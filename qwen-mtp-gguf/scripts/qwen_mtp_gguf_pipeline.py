#!/usr/bin/env python3
"""Plan, validate, extract Qwen MTP heads, build GGUF quants, smoke-test, and upload."""

from __future__ import annotations

import argparse
import fnmatch
import importlib.util
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any, Iterable

MISSING_DEPS: list[str] = []
try:
    from huggingface_hub import HfApi, create_repo, hf_hub_download, snapshot_download
except ImportError:
    HfApi = create_repo = hf_hub_download = snapshot_download = None  # type: ignore[assignment]
    MISSING_DEPS.append("huggingface_hub")

try:
    from safetensors import safe_open
    from safetensors.torch import save_file
except ImportError:
    safe_open = save_file = None  # type: ignore[assignment]
    MISSING_DEPS.append("safetensors")


DEFAULT_QUANTS = [
    "q2_k",
    "q3_k_s",
    "q3_k_m",
    "q3_k_l",
    "iq4_xs",
    "q4_k_s",
    "q4_k_m",
    "q5_k_s",
    "q5_k_m",
    "q6_k",
    "q8_0",
    "bf16",
]

TARGET_ALLOW_PATTERNS = [
    "*.json",
    "*.safetensors",
    "*.model",
    "*.txt",
    "*.py",
    "*.tiktoken",
    "*.jinja",
    "*.md",
]

TARGET_IGNORE_PATTERNS = [
    "*.gguf",
    "*.pt",
    "*.pth",
    "*.bin",
    "*.onnx",
    "*.ckpt",
    "optimizer*",
    "scheduler*",
    "runs/*",
    "wandb/*",
    "checkpoint*",
    "*.log",
]

# Approximate bits per weight. The preflight uses these for conservative disk estimates only.
QUANT_BPW = {
    "q2_k": 2.80,
    "q3_k_s": 3.45,
    "q3_k_m": 3.70,
    "q3_k_l": 4.05,
    "iq4_xs": 4.25,
    "q4_k_s": 4.60,
    "q4_k_m": 4.85,
    "q5_k_s": 5.50,
    "q5_k_m": 5.75,
    "q6_k": 6.70,
    "q8_0": 8.50,
    "f16": 16.0,
    "bf16": 16.0,
}

CONFIG_COMPAT_FIELDS = [
    "model_type",
    "architectures",
    "hidden_size",
    "num_hidden_layers",
    "num_attention_heads",
    "num_key_value_heads",
    "intermediate_size",
    "vocab_size",
    "rope_theta",
    "max_position_embeddings",
]


@dataclass
class Job:
    source_repo: str | None
    source_dir: Path | None
    mtp_source_repo: str
    output_repo: str | None
    filename_prefix: str
    prepared_dir: Path
    work_dir: Path
    quant_types: list[str] = field(default_factory=lambda: DEFAULT_QUANTS.copy())
    reusable_mtp_heads: list[Path] = field(default_factory=list)


@dataclass
class RepoSizing:
    total_bytes: int = 0
    safetensors_bytes: int = 0
    selected_files: int = 0
    file_sizes: dict[str, int] = field(default_factory=dict)


@dataclass
class Estimate:
    target_bytes: int
    source_mtp_bytes: int
    f16_bytes: int
    output_bytes: dict[str, int]
    required_work_bytes: int
    recommended_ram_bytes: int
    strategy: str


def now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def log(message: str, log_path: Path | None = None) -> None:
    line = f"[{now()}] {message}"
    print(line, flush=True)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def fmt_bytes(value: int | float | None) -> str:
    if value is None:
        return "unknown"
    value = float(value)
    for unit in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if abs(value) < 1024 or unit == "TiB":
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} TiB"


def normalize_quant_types(value: str | list[str] | None) -> list[str]:
    if value is None:
        return DEFAULT_QUANTS.copy()
    if isinstance(value, str):
        items = [part.strip() for part in value.split(",") if part.strip()]
    else:
        items = [str(part).strip() for part in value if str(part).strip()]
    return [item.lower() for item in items]


def safe_name(value: str) -> str:
    value = value.split("/")[-1]
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return value or "qwen-mtp"


def file_size_gb(path: Path) -> float:
    return path.stat().st_size / (1024**3)


def tree_size(path: Path, patterns: list[str] | None = None) -> int:
    if path.is_file():
        return path.stat().st_size
    total = 0
    for item in path.rglob("*"):
        if not item.is_file():
            continue
        rel = item.relative_to(path).as_posix()
        if patterns and not any(fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(item.name, pattern) for pattern in patterns):
            continue
        total += item.stat().st_size
    return total


def existing_ancestor(path: Path) -> Path:
    path = path.expanduser().resolve()
    while not path.exists() and path != path.parent:
        path = path.parent
    return path


def disk_free_bytes(path: Path) -> int:
    return shutil.disk_usage(existing_ancestor(path)).free


def total_ram_bytes() -> int | None:
    try:
        if hasattr(os, "sysconf"):
            pages = os.sysconf("SC_PHYS_PAGES")
            page_size = os.sysconf("SC_PAGE_SIZE")
            return int(pages * page_size)
    except (OSError, ValueError, AttributeError):
        pass
    if platform.system() == "Darwin":
        try:
            out = subprocess.check_output(["sysctl", "-n", "hw.memsize"], text=True).strip()
            return int(out)
        except Exception:
            return None
    return None


def command_output(cmd: list[str], timeout: int = 5) -> str | None:
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT, timeout=timeout).strip()
    except Exception:
        return None


def detect_environment(llama_cpp: Path, token_available: bool) -> dict[str, Any]:
    gpu = command_output(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"], timeout=5)
    if not gpu and platform.system() == "Darwin":
        gpu = command_output(["sysctl", "-n", "machdep.cpu.brand_string"], timeout=5)
    return {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "python": sys.version.split()[0],
        "cpu_count": os.cpu_count(),
        "ram_bytes": total_ram_bytes(),
        "gpu_hint": gpu or "not detected or not required",
        "commands": {name: bool(shutil.which(name)) for name in ["git", "cmake", "make", "ninja", "python3", "pip"]},
        "packages": {
            name: importlib.util.find_spec(name) is not None
            for name in ["huggingface_hub", "safetensors", "transformers", "torch"]
        },
        "llama_cpp": str(llama_cpp),
        "convert_hf_to_gguf": (llama_cpp / "convert_hf_to_gguf.py").exists(),
        "llama_quantize": (llama_cpp / "build/bin/llama-quantize").exists(),
        "llama_cli": (llama_cpp / "build/bin/llama-cli").exists(),
        "hf_token_available": token_available,
    }


def load_token(args: argparse.Namespace) -> str | None:
    if args.token_env and os.environ.get(args.token_env):
        return os.environ[args.token_env]
    if args.token_file:
        token_path = Path(args.token_file).expanduser()
        if not token_path.exists():
            raise FileNotFoundError(token_path)
        for line in token_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if "=" in stripped:
                key, value = stripped.split("=", 1)
                if key.strip() == args.token_file_key:
                    return value.strip().strip('"').strip("'")
            elif args.token_file_key == "HF_TOKEN":
                return stripped.strip('"').strip("'")
    return None


def require_runtime_deps() -> None:
    if MISSING_DEPS:
        missing = ", ".join(MISSING_DEPS)
        raise RuntimeError(
            f"Missing required Python packages: {missing}. "
            "Run scripts/bootstrap_qwen_mtp_env.sh or install huggingface_hub and safetensors."
        )


def run_command(cmd: list[str], log_path: Path, env: dict[str, str] | None = None) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8", errors="replace") as f:
        f.write(f"\n[{now()}] RUN {' '.join(cmd)}\n")
        f.flush()
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            bufsize=1,
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            f.write(line)
            f.flush()
        rc = proc.wait()
        f.write(f"[{now()}] EXIT {rc}\n")
    if rc != 0:
        raise subprocess.CalledProcessError(rc, cmd)


def matches_any(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(Path(path).name, pattern) for pattern in patterns)


def repo_sizing(repo_id: str, token: str | None, allow_patterns: list[str], ignore_patterns: list[str]) -> RepoSizing:
    api = HfApi(token=token)
    info = api.model_info(repo_id=repo_id, files_metadata=True, token=token)
    result = RepoSizing()
    for sibling in info.siblings:
        name = sibling.rfilename
        if allow_patterns and not matches_any(name, allow_patterns):
            continue
        if ignore_patterns and matches_any(name, ignore_patterns):
            continue
        size = getattr(sibling, "size", None)
        if size is None and getattr(sibling, "lfs", None):
            size = sibling.lfs.get("size")
        if size is None:
            continue
        result.file_sizes[name] = int(size)
        result.total_bytes += int(size)
        result.selected_files += 1
        if name.endswith(".safetensors"):
            result.safetensors_bytes += int(size)
    return result


def safe_shard_name(name: Any) -> str:
    """Reject shard names from an untrusted index that are not plain relative in-directory paths."""
    if (
        not isinstance(name, str)
        or not name
        or "\x00" in name
        or not name.endswith(".safetensors")
        or PurePosixPath(name).is_absolute()
        or PureWindowsPath(name).is_absolute()
        or PureWindowsPath(name).drive
        or ".." in PurePosixPath(name.replace("\\", "/")).parts
    ):
        raise RuntimeError(f"Unsafe shard name in index: {name!r}")
    return name


def safe_shard_path(base: Path, name: Any) -> Path:
    name = safe_shard_name(name)
    base_abs = os.path.abspath(base)
    path = os.path.abspath(os.path.join(base_abs, name))
    if os.path.commonpath([path, base_abs]) != base_abs:
        raise RuntimeError(f"Shard escapes model directory: {name!r}")
    return Path(path)


def source_mtp_shards(repo_id: str, token: str | None) -> tuple[list[str], list[str]]:
    index_path = hf_hub_download(repo_id=repo_id, filename="model.safetensors.index.json", token=token)
    index_data = json.loads(Path(index_path).read_text(encoding="utf-8"))
    weight_map = index_data.get("weight_map", {})
    mtp_keys = sorted(
        key for key in weight_map if "mtp" in key.lower() or "nextn" in key.lower()
    )
    if not mtp_keys:
        raise RuntimeError(f"No MTP or nextn tensors listed in {repo_id} index")
    return mtp_keys, sorted({safe_shard_name(weight_map[key]) for key in mtp_keys})


def load_config_from_repo(repo_id: str, token: str | None) -> dict[str, Any]:
    path = hf_hub_download(repo_id=repo_id, filename="config.json", token=token)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_config_from_dir(path: Path) -> dict[str, Any]:
    config_path = path / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(config_path)
    return json.loads(config_path.read_text(encoding="utf-8"))


def compare_configs(job: Job, token: str | None) -> list[str]:
    target_config = load_config_from_repo(job.source_repo, token) if job.source_repo else load_config_from_dir(job.source_dir or job.prepared_dir)
    mtp_config = load_config_from_repo(job.mtp_source_repo, token)
    mismatches = []
    for field_name in CONFIG_COMPAT_FIELDS:
        if field_name in target_config and field_name in mtp_config and target_config[field_name] != mtp_config[field_name]:
            mismatches.append(f"{field_name}: target={target_config[field_name]!r}, mtp_source={mtp_config[field_name]!r}")
    return mismatches


def estimate_job(job: Job, token: str | None, strategy: str, safety_factor: float) -> Estimate:
    if job.source_repo:
        target = repo_sizing(job.source_repo, token, TARGET_ALLOW_PATTERNS, TARGET_IGNORE_PATTERNS)
        target_bytes = target.total_bytes
        safetensors_bytes = target.safetensors_bytes or target.total_bytes
    else:
        target_bytes = tree_size(job.source_dir or job.prepared_dir)
        safetensors_bytes = tree_size(job.source_dir or job.prepared_dir, ["*.safetensors"]) or target_bytes

    _, mtp_shards = source_mtp_shards(job.mtp_source_repo, token)
    mtp_repo = repo_sizing(job.mtp_source_repo, token, ["model.safetensors.index.json", "*.safetensors"], [])
    source_mtp_bytes = sum(mtp_repo.file_sizes.get(name, 0) for name in mtp_shards)
    source_mtp_bytes += mtp_repo.file_sizes.get("model.safetensors.index.json", 0)

    f16_bytes = int(max(safetensors_bytes, target_bytes * 0.9) * 1.05)
    output_bytes: dict[str, int] = {}
    for qtype in job.quant_types:
        bpw = QUANT_BPW.get(qtype.lower(), 8.0)
        output_bytes[qtype] = int(f16_bytes * (bpw / 16.0) * 1.10)

    if strategy == "batch":
        live_outputs = sum(output_bytes.values())
    elif strategy == "local-only":
        live_outputs = sum(output_bytes.values())
    else:
        live_outputs = max(output_bytes.values(), default=0)

    non_bf16_needed = any(qtype != "bf16" for qtype in job.quant_types)
    temp_f16_bytes = f16_bytes if non_bf16_needed else 0
    required_work_bytes = int((target_bytes + source_mtp_bytes + temp_f16_bytes + live_outputs) * safety_factor)
    recommended_ram_bytes = int(max(16 * 1024**3, min(f16_bytes * 1.15, f16_bytes + 32 * 1024**3)))
    return Estimate(
        target_bytes=target_bytes,
        source_mtp_bytes=source_mtp_bytes,
        f16_bytes=f16_bytes,
        output_bytes=output_bytes,
        required_work_bytes=required_work_bytes,
        recommended_ram_bytes=recommended_ram_bytes,
        strategy=strategy,
    )


def write_preflight_report(
    job: Job,
    env_info: dict[str, Any],
    estimate: Estimate,
    config_mismatches: list[str],
    log_path: Path,
) -> None:
    free_work = disk_free_bytes(job.work_dir)
    ram = env_info["ram_bytes"]
    lines = [
        f"# Preflight report for {job.filename_prefix}",
        "",
        f"- Source: `{job.source_repo or job.source_dir}`",
        f"- MTP source: `{job.mtp_source_repo}`",
        f"- Output repo: `{job.output_repo or 'local only'}`",
        f"- Work directory: `{job.work_dir}`",
        f"- Upload strategy: `{estimate.strategy}`",
        "",
        "## Environment",
        f"- Platform: {env_info['platform']} ({env_info['machine']})",
        f"- Python: {env_info['python']}",
        f"- CPU cores: {env_info['cpu_count']}",
        f"- RAM: {fmt_bytes(ram)}",
        f"- GPU hint: {env_info['gpu_hint']}",
        f"- llama.cpp: `{env_info['llama_cpp']}`",
        f"- converter present: {env_info['convert_hf_to_gguf']}",
        f"- quantizer present: {env_info['llama_quantize']}",
        f"- llama-cli present: {env_info['llama_cli']}",
        f"- HF token available: {env_info['hf_token_available']}",
        "",
        "## Size Estimate",
        f"- Target model download/prepared size: {fmt_bytes(estimate.target_bytes)}",
        f"- Minimal MTP source shards: {fmt_bytes(estimate.source_mtp_bytes)}",
        f"- Temporary F16 GGUF estimate: {fmt_bytes(estimate.f16_bytes)}",
        f"- Required free disk estimate with margin: {fmt_bytes(estimate.required_work_bytes)}",
        f"- Free disk at work directory: {fmt_bytes(free_work)}",
        f"- Recommended RAM for conversion/quantization: {fmt_bytes(estimate.recommended_ram_bytes)}",
        "",
        "## Output Estimates",
    ]
    for qtype, size in estimate.output_bytes.items():
        lines.append(f"- {qtype.upper()}: {fmt_bytes(size)}")
    lines.append("")
    lines.append("## Compatibility")
    if config_mismatches:
        lines.append("Potential target/base config mismatches:")
        lines.extend(f"- {item}" for item in config_mismatches)
    else:
        lines.append("No checked config mismatches detected.")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def preflight_job(job: Job, token: str | None, llama_cpp: Path, args: argparse.Namespace) -> Estimate:
    job.work_dir.mkdir(parents=True, exist_ok=True)
    report_path = job.work_dir / "preflight_report.md"
    env_info = detect_environment(llama_cpp, token is not None)
    estimate = estimate_job(job, token, args.upload_strategy, args.disk_safety_factor)
    config_mismatches = compare_configs(job, token)
    write_preflight_report(job, env_info, estimate, config_mismatches, report_path)
    log(f"Wrote preflight report: {report_path}")

    problems = []
    if not env_info["convert_hf_to_gguf"]:
        problems.append(f"Missing llama.cpp converter: {llama_cpp / 'convert_hf_to_gguf.py'}")
    if not env_info["llama_quantize"] and any(qtype != "bf16" for qtype in job.quant_types):
        problems.append(f"Missing llama.cpp quantizer: {llama_cpp / 'build/bin/llama-quantize'}")
    if job.output_repo and not token:
        problems.append("HF token is required for uploading to output_repo")
    if config_mismatches and not args.allow_config_mismatch:
        problems.append("Target and MTP source config fields differ; use --allow-config-mismatch only after manual review")

    free_work = disk_free_bytes(job.work_dir)
    if free_work < estimate.required_work_bytes and not args.allow_insufficient_disk:
        problems.append(
            f"Insufficient disk at {job.work_dir}: need about {fmt_bytes(estimate.required_work_bytes)}, "
            f"found {fmt_bytes(free_work)}"
        )

    ram = env_info["ram_bytes"]
    if ram and ram < estimate.recommended_ram_bytes and not args.allow_low_ram:
        problems.append(
            f"RAM may be insufficient: recommended {fmt_bytes(estimate.recommended_ram_bytes)}, "
            f"found {fmt_bytes(ram)}. Use --allow-low-ram to continue."
        )

    if problems:
        for problem in problems:
            log(f"PREFLIGHT BLOCKER: {problem}")
        raise RuntimeError("Preflight failed; see preflight_report.md")
    return estimate


def list_mtp_keys_from_index(model_dir: Path) -> tuple[list[str], dict[str, str]]:
    index_path = model_dir / "model.safetensors.index.json"
    if not index_path.exists():
        return [], {}
    index_data = json.loads(index_path.read_text(encoding="utf-8"))
    weight_map = index_data.get("weight_map", {})
    mtp_keys = sorted(
        key for key in weight_map if "mtp" in key.lower() or "nextn" in key.lower()
    )
    return mtp_keys, weight_map


def scan_mtp_keys_without_index(model_dir: Path) -> list[str]:
    keys: list[str] = []
    for shard in sorted(model_dir.glob("*.safetensors")):
        with safe_open(str(shard), framework="pt", device="cpu") as f:
            keys.extend(
                key for key in f.keys() if "mtp" in key.lower() or "nextn" in key.lower()
            )
    return sorted(keys)


def build_index_from_local_shards(model_dir: Path, job_log: Path) -> None:
    index_path = model_dir / "model.safetensors.index.json"
    weight_map: dict[str, str] = {}
    total_size = 0
    for shard in sorted(model_dir.glob("*.safetensors")):
        total_size += shard.stat().st_size
        with safe_open(str(shard), framework="pt", device="cpu") as f:
            for key in f.keys():
                weight_map[key] = shard.name
    if not weight_map:
        raise RuntimeError(f"No safetensors shards found in {model_dir}")
    index_data = {"metadata": {"total_size": total_size}, "weight_map": weight_map}
    index_path.write_text(json.dumps(index_data, indent=2) + "\n", encoding="utf-8")
    log(f"Built model.safetensors.index.json with {len(weight_map)} tensor mappings.", job_log)


def validate_indexed_tensors(model_dir: Path, keys: Iterable[str], weight_map: dict[str, str]) -> None:
    by_file: dict[str, list[str]] = {}
    for key in keys:
        filename = weight_map.get(key)
        if not filename:
            raise RuntimeError(f"Index is missing weight_map entry for {key}")
        by_file.setdefault(filename, []).append(key)
    for filename, expected_keys in sorted(by_file.items()):
        shard = safe_shard_path(model_dir, filename)
        if not shard.exists():
            raise FileNotFoundError(f"Indexed shard does not exist: {filename}")
        with safe_open(str(shard), framework="pt", device="cpu") as f:
            available = set(f.keys())
        missing = sorted(set(expected_keys) - available)
        if missing:
            raise RuntimeError(f"{filename} is missing indexed tensors: {missing[:10]}")


def model_has_valid_mtp(model_dir: Path, job_log: Path) -> bool:
    mtp_keys, weight_map = list_mtp_keys_from_index(model_dir)
    if mtp_keys:
        validate_indexed_tensors(model_dir, mtp_keys, weight_map)
        shards = sorted({weight_map[key] for key in mtp_keys})
        log(f"Detected {len(mtp_keys)} existing MTP tensors in index: {shards}", job_log)
        return True
    scanned = scan_mtp_keys_without_index(model_dir)
    if scanned:
        if not (model_dir / "model.safetensors.index.json").exists():
            build_index_from_local_shards(model_dir, job_log)
        mtp_keys, weight_map = list_mtp_keys_from_index(model_dir)
        validate_indexed_tensors(model_dir, mtp_keys, weight_map)
        log(f"Detected {len(scanned)} existing MTP tensors by safetensors scan.", job_log)
        return True
    return False


def copy_reusable_mtp_heads(job: Job, target_path: Path, job_log: Path) -> bool:
    for source in job.reusable_mtp_heads:
        if not source.exists():
            continue
        with safe_open(str(source), framework="pt", device="cpu") as f:
            keys = list(f.keys())
        if keys:
            shutil.copy2(source, target_path)
            log(f"Reused {len(keys)} MTP tensors from {source}.", job_log)
            return True
    return False


def extract_mtp_heads(job: Job, token: str | None, target_path: Path, job_log: Path) -> None:
    if copy_reusable_mtp_heads(job, target_path, job_log):
        return
    mtp_keys, shards = source_mtp_shards(job.mtp_source_repo, token)
    allow_patterns = ["model.safetensors.index.json", *shards]
    log(f"Downloading MTP shards from {job.mtp_source_repo}: {shards}", job_log)
    snapshot_dir = Path(
        snapshot_download(
            repo_id=job.mtp_source_repo,
            allow_patterns=allow_patterns,
            token=token,
            max_workers=8,
        )
    )
    wanted = set(mtp_keys)
    tensors = {}
    for shard_name in shards:
        shard_path = safe_shard_path(snapshot_dir, shard_name)
        with safe_open(str(shard_path), framework="pt", device="cpu") as f:
            for key in f.keys():
                if key in wanted:
                    tensors[key] = f.get_tensor(key)
    missing = sorted(wanted - set(tensors))
    if missing:
        raise RuntimeError(f"Missing extracted MTP tensors: {missing[:10]}")
    save_file(tensors, str(target_path))
    log(f"Extracted {len(tensors)} MTP tensors to {target_path}.", job_log)


def inject_mtp_index(model_dir: Path, mtp_path: Path, job_log: Path) -> None:
    index_path = model_dir / "model.safetensors.index.json"
    if not index_path.exists():
        build_index_from_local_shards(model_dir, job_log)
    backup_path = model_dir / "model.safetensors.index.pre_mtp_backup.json"
    if not backup_path.exists():
        shutil.copy2(index_path, backup_path)
    index_data = json.loads(index_path.read_text(encoding="utf-8"))
    weight_map = index_data.setdefault("weight_map", {})
    with safe_open(str(mtp_path), framework="pt", device="cpu") as f:
        mtp_keys = list(f.keys())
    for key in mtp_keys:
        weight_map[key] = mtp_path.name
    index_path.write_text(json.dumps(index_data, indent=2) + "\n", encoding="utf-8")
    validate_indexed_tensors(model_dir, mtp_keys, weight_map)
    log(f"Injected {len(mtp_keys)} MTP tensor mappings into {index_path}.", job_log)


def ensure_mtp(job: Job, token: str | None, job_log: Path) -> None:
    if model_has_valid_mtp(job.prepared_dir, job_log):
        return
    mtp_path = job.prepared_dir / "mtp_heads.safetensors"
    extract_mtp_heads(job, token, mtp_path, job_log)
    inject_mtp_index(job.prepared_dir, mtp_path, job_log)
    if not model_has_valid_mtp(job.prepared_dir, job_log):
        raise RuntimeError("MTP injection did not validate")


def prepare_target(job: Job, token: str | None, job_log: Path) -> None:
    job.prepared_dir.mkdir(parents=True, exist_ok=True)
    if job.source_repo:
        log(f"Downloading or refreshing {job.source_repo} into {job.prepared_dir}.", job_log)
        snapshot_download(
            repo_id=job.source_repo,
            local_dir=str(job.prepared_dir),
            allow_patterns=TARGET_ALLOW_PATTERNS,
            ignore_patterns=TARGET_IGNORE_PATTERNS,
            token=token,
            max_workers=8,
        )
    elif job.source_dir:
        if not job.source_dir.exists():
            raise FileNotFoundError(job.source_dir)
        if job.source_dir.resolve() != job.prepared_dir.resolve():
            log(f"Copying local source {job.source_dir} to {job.prepared_dir}.", job_log)
            shutil.copytree(job.source_dir, job.prepared_dir, dirs_exist_ok=True)
    else:
        raise RuntimeError("Job must provide source_repo or source_dir")


def ensure_repo(api: HfApi, repo_id: str, token: str | None, private: bool, job_log: Path) -> set[str]:
    if not token:
        raise RuntimeError("HF token is required for upload")
    create_repo(repo_id=repo_id, repo_type="model", private=private, token=token, exist_ok=True)
    try:
        if private:
            api.update_repo_settings(repo_id=repo_id, private=True, token=token)
    except Exception as exc:
        log(f"Repo privacy update skipped or failed: {exc}", job_log)
    existing = set(api.list_repo_files(repo_id=repo_id, repo_type="model", token=token))
    log(f"Remote repo has {len(existing)} files.", job_log)
    return existing


def upload_with_retries(
    api: HfApi,
    token: str | None,
    local_path: Path,
    path_in_repo: str,
    repo_id: str,
    job_log: Path,
    max_retries: int,
) -> None:
    if not token:
        raise RuntimeError("HF token is required for upload")
    size_gb = file_size_gb(local_path)
    for attempt in range(1, max_retries + 1):
        try:
            log(f"Upload attempt {attempt}/{max_retries}: {path_in_repo} ({size_gb:.2f} GB).", job_log)
            start = time.time()
            api.upload_file(
                path_or_fileobj=str(local_path),
                path_in_repo=path_in_repo,
                repo_id=repo_id,
                repo_type="model",
                token=token,
            )
            elapsed = max(time.time() - start, 0.001)
            log(f"Uploaded {path_in_repo} in {elapsed:.1f}s at {size_gb * 1024 / elapsed:.1f} MB/s.", job_log)
            return
        except Exception as exc:
            log(f"Upload failed: {exc}", job_log)
            if attempt == max_retries:
                raise
            wait = min(60 * attempt, 600)
            log(f"Waiting {wait}s before retry.", job_log)
            time.sleep(wait)


def gguf_name(job: Job, qtype: str) -> str:
    return f"{job.filename_prefix}-{qtype.upper()}.gguf"


def write_readme(job: Job, api: HfApi, token: str | None, private: bool, job_log: Path, max_retries: int) -> None:
    if not job.output_repo:
        return
    source_label = job.source_repo or str(job.source_dir)
    readme = job.work_dir / "README.md"
    lines = [
        "---",
        "license: other",
        f"private: {'true' if private else 'false'}",
        "---",
        "",
        f"# {job.output_repo}",
        "",
        f"Source model: `{source_label}`",
        f"MTP source: `{job.mtp_source_repo}`",
        "",
        "Uploaded GGUF variants:",
        "",
    ]
    lines.extend(f"- `{gguf_name(job, qtype)}`" for qtype in job.quant_types)
    lines.extend(
        [
            "",
            "This release was prepared by validating or injecting Qwen MTP/nextn tensors before GGUF conversion.",
            "",
        ]
    )
    readme.write_text("\n".join(lines), encoding="utf-8")
    upload_with_retries(api, token, readme, "README.md", job.output_repo, job_log, min(max_retries, 3))


def convert_f16(job: Job, llama_cpp: Path, job_log: Path, quant_types: list[str]) -> Path | None:
    non_bf16 = [q for q in quant_types if q != "bf16"]
    if not non_bf16:
        return None
    f16_path = job.work_dir / f"{job.filename_prefix}-F16.gguf"
    if f16_path.exists() and f16_path.stat().st_size > 0:
        log(f"Reusing temporary F16 GGUF: {f16_path} ({file_size_gb(f16_path):.2f} GB).", job_log)
        return f16_path
    env = os.environ.copy()
    env["PYTHONPATH"] = str(llama_cpp / "gguf-py")
    run_command(
        [
            "python3",
            str(llama_cpp / "convert_hf_to_gguf.py"),
            str(job.prepared_dir),
            "--outfile",
            str(f16_path),
            "--outtype",
            "f16",
        ],
        job.work_dir / "convert_f16.log",
        env=env,
    )
    log(f"Created temporary F16 GGUF: {f16_path} ({file_size_gb(f16_path):.2f} GB).", job_log)
    return f16_path


def convert_bf16(job: Job, llama_cpp: Path, output_path: Path, job_log: Path) -> None:
    if output_path.exists() and output_path.stat().st_size > 0:
        log(f"Reusing BF16 GGUF: {output_path} ({file_size_gb(output_path):.2f} GB).", job_log)
        return
    env = os.environ.copy()
    env["PYTHONPATH"] = str(llama_cpp / "gguf-py")
    run_command(
        [
            "python3",
            str(llama_cpp / "convert_hf_to_gguf.py"),
            str(job.prepared_dir),
            "--outfile",
            str(output_path),
            "--outtype",
            "bf16",
        ],
        job.work_dir / "convert_bf16.log",
        env=env,
    )


def quantize(job: Job, llama_cpp: Path, f16_path: Path, qtype: str, output_path: Path, job_log: Path) -> None:
    if output_path.exists() and output_path.stat().st_size > 0:
        log(f"Reusing {qtype.upper()} GGUF: {output_path} ({file_size_gb(output_path):.2f} GB).", job_log)
        return
    run_command(
        [
            str(llama_cpp / "build/bin/llama-quantize"),
            str(f16_path),
            str(output_path),
            qtype.upper(),
        ],
        job.work_dir / f"quant_{qtype.upper()}.log",
    )


def fallback_chatml_prompt(user_prompt: str, system_prompt: str) -> str:
    return (
        f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
        f"<|im_start|>user\n{user_prompt}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )


def smoke_test_gguf(
    llama_cpp: Path,
    model_path: Path,
    prompt: str,
    system_prompt: str,
    max_tokens: int,
    ctx_size: int,
    job_log: Path,
) -> None:
    llama_cli = llama_cpp / "build/bin/llama-cli"
    if not llama_cli.exists():
        raise FileNotFoundError(f"llama-cli not found for smoke test: {llama_cli}")
    command = [
        str(llama_cli),
        "-m",
        str(model_path),
        "-p",
        fallback_chatml_prompt(prompt, system_prompt),
        "-n",
        str(max_tokens),
        "-c",
        str(ctx_size),
        "--temp",
        "0.2",
        "--top-p",
        "0.9",
        "-ngl",
        "0",
    ]
    log(f"Running CPU GGUF smoke test on {model_path.name}.", job_log)
    run_command(command, job_log.parent / f"smoke_{model_path.stem}.log")
    log(f"Smoke test completed for {model_path.name}.", job_log)


def cleanup_job(job: Job, uploaded: set[str], job_log: Path) -> None:
    expected = {gguf_name(job, qtype) for qtype in job.quant_types}
    missing = expected - uploaded
    if missing:
        log(f"Skipping cleanup because uploads are missing: {sorted(missing)}", job_log)
        return
    for path in job.work_dir.glob("*.gguf"):
        path.unlink()
        log(f"Removed local GGUF: {path.name}", job_log)
    f16_path = job.work_dir / f"{job.filename_prefix}-F16.gguf"
    if f16_path.exists():
        f16_path.unlink()
    if job.prepared_dir.exists():
        shutil.rmtree(job.prepared_dir)
        log(f"Removed prepared HF directory: {job.prepared_dir}", job_log)


def process_job(
    job: Job,
    token: str | None,
    llama_cpp: Path,
    private: bool,
    cleanup_after_upload: bool,
    max_retries: int,
    args: argparse.Namespace,
) -> None:
    job.work_dir.mkdir(parents=True, exist_ok=True)
    job_log = job.work_dir / "pipeline.log"
    log(f"===== Starting {job.filename_prefix} =====", job_log)

    if not args.skip_preflight:
        preflight_job(job, token, llama_cpp, args)

    prepare_target(job, token, job_log)
    ensure_mtp(job, token, job_log)

    api = HfApi(token=token) if (job.output_repo and args.upload_strategy != "local-only") else None
    remote_existing: set[str] = set()
    if job.output_repo and api is not None:
        try:
            remote_existing = set(api.list_repo_files(repo_id=job.output_repo, repo_type="model", token=token))
        except Exception:
            pass

    uploaded = set(remote_existing)
    if job.output_repo and api is not None:
        remaining = [qtype for qtype in job.quant_types if gguf_name(job, qtype) not in uploaded]
    else:
        remaining = job.quant_types
    if not remaining:
        log("All expected GGUF files already exist remotely.", job_log)
        if cleanup_after_upload and job.output_repo and args.upload_strategy != "local-only":
            cleanup_job(job, uploaded, job_log)
        log(f"===== Finished {job.filename_prefix} =====", job_log)
        return

    f16_path = convert_f16(job, llama_cpp, job_log, remaining)
    if args.smoke_test_before_upload and f16_path is not None:
        smoke_test_gguf(
            llama_cpp=llama_cpp,
            model_path=f16_path,
            prompt=args.smoke_prompt,
            system_prompt=args.smoke_system_prompt,
            max_tokens=args.smoke_max_tokens,
            ctx_size=args.smoke_ctx_size,
            job_log=job_log,
        )

    # Delay repository creation and README writing until conversion and smoke tests succeed
    if job.output_repo and api is not None:
        remote_existing = ensure_repo(api, job.output_repo, token, private, job_log)
        write_readme(job, api, token, private, job_log, max_retries)
        uploaded.update(remote_existing)


    local_outputs: list[Path] = []
    for qtype in job.quant_types:
        filename = gguf_name(job, qtype)
        output_path = job.work_dir / filename
        if filename in uploaded:
            log(f"Remote already has {filename}; skipping.", job_log)
            continue
        if qtype == "bf16":
            convert_bf16(job, llama_cpp, output_path, job_log)
        else:
            if f16_path is None:
                raise RuntimeError(f"F16 source missing for {qtype}")
            quantize(job, llama_cpp, f16_path, qtype, output_path, job_log)

        if args.smoke_test_each_output:
            smoke_test_gguf(
                llama_cpp=llama_cpp,
                model_path=output_path,
                prompt=args.smoke_prompt,
                system_prompt=args.smoke_system_prompt,
                max_tokens=args.smoke_max_tokens,
                ctx_size=args.smoke_ctx_size,
                job_log=job_log,
            )

        if job.output_repo and api is not None and args.upload_strategy == "stream":
            upload_with_retries(api, token, output_path, filename, job.output_repo, job_log, max_retries)
            uploaded.add(filename)
            output_path.unlink(missing_ok=True)
            log(f"Removed local file after upload: {filename}", job_log)
        else:
            local_outputs.append(output_path)

    if job.output_repo and api is not None and args.upload_strategy == "batch":
        for output_path in local_outputs:
            filename = output_path.name
            if filename in uploaded:
                continue
            upload_with_retries(api, token, output_path, filename, job.output_repo, job_log, max_retries)
            uploaded.add(filename)
            if cleanup_after_upload:
                output_path.unlink(missing_ok=True)
                log(f"Removed local file after upload: {filename}", job_log)

    if cleanup_after_upload and job.output_repo:
        cleanup_job(job, uploaded, job_log)
    log(f"===== Finished {job.filename_prefix} =====", job_log)


def job_from_mapping(raw: dict[str, Any], defaults: dict[str, Any], args: argparse.Namespace) -> Job:
    data = {**defaults, **raw}
    source_repo = data.get("source_repo")
    source_dir = Path(data["source_dir"]).expanduser() if data.get("source_dir") else None
    mtp_source_repo = data.get("mtp_source_repo")
    if not mtp_source_repo:
        raise ValueError("Each job requires mtp_source_repo")
    output_repo = data.get("output_repo")
    work_root = Path(data.get("work_root") or args.work_root).expanduser()
    prefix = data.get("filename_prefix") or f"{safe_name(source_repo or str(source_dir))}-MTP"
    prepared_dir = Path(data["prepared_dir"]).expanduser() if data.get("prepared_dir") else work_root / f"{safe_name(prefix)}-HF"
    work_dir = Path(data["work_dir"]).expanduser() if data.get("work_dir") else work_root / f"{safe_name(prefix)}-GGUF"
    reusable = [Path(path).expanduser() for path in data.get("reusable_mtp_heads", [])]
    return Job(
        source_repo=source_repo,
        source_dir=source_dir,
        mtp_source_repo=mtp_source_repo,
        output_repo=output_repo,
        filename_prefix=prefix,
        prepared_dir=prepared_dir,
        work_dir=work_dir,
        quant_types=normalize_quant_types(data.get("quant_types") or args.quant_types),
        reusable_mtp_heads=reusable,
    )


def load_jobs(args: argparse.Namespace) -> list[Job]:
    if args.jobs:
        data = json.loads(Path(args.jobs).read_text(encoding="utf-8"))
        if isinstance(data, list):
            defaults: dict[str, Any] = {}
            jobs_raw = data
        else:
            defaults = data.get("defaults", {})
            jobs_raw = data.get("jobs", [])
        return [job_from_mapping(item, defaults, args) for item in jobs_raw]

    raw = {
        "source_repo": args.source_repo,
        "source_dir": args.source_dir,
        "mtp_source_repo": args.mtp_source_repo,
        "output_repo": args.output_repo,
        "filename_prefix": args.filename_prefix,
        "prepared_dir": args.prepared_dir,
        "work_dir": args.work_dir,
    }
    return [job_from_mapping(raw, {}, args)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", help="JSON file with defaults and jobs")
    parser.add_argument("--source-repo")
    parser.add_argument("--source-dir")
    parser.add_argument("--mtp-source-repo")
    parser.add_argument("--output-repo")
    parser.add_argument("--filename-prefix")
    parser.add_argument("--prepared-dir")
    parser.add_argument("--work-dir")
    parser.add_argument("--work-root", default="./qwen-mtp-gguf-work")
    parser.add_argument("--llama-cpp", required=True)
    parser.add_argument("--quant-types", default=",".join(DEFAULT_QUANTS))
    parser.add_argument("--token-env", default="HF_TOKEN")
    parser.add_argument("--token-file")
    parser.add_argument("--token-file-key", default="HF_TOKEN")
    parser.add_argument("--private", action="store_true", help="Create/update output repos as private")
    parser.add_argument("--cleanup-after-upload", action="store_true")
    parser.add_argument("--max-upload-retries", type=int, default=8)
    parser.add_argument("--upload-strategy", choices=["stream", "batch", "local-only"], default="stream")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--skip-preflight", action="store_true")
    parser.add_argument("--disk-safety-factor", type=float, default=1.25)
    parser.add_argument("--allow-insufficient-disk", action="store_true")
    parser.add_argument("--allow-low-ram", action="store_true")
    parser.add_argument("--allow-config-mismatch", action="store_true")
    parser.add_argument("--smoke-test-before-upload", action="store_true")
    parser.add_argument("--smoke-test-each-output", action="store_true")
    parser.add_argument("--smoke-prompt", default="Write one concise sentence explaining what MTP adds to a language model.")
    parser.add_argument("--smoke-system-prompt", default="You are a helpful AI assistant.")
    parser.add_argument("--smoke-max-tokens", type=int, default=96)
    parser.add_argument("--smoke-ctx-size", type=int, default=2048)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    require_runtime_deps()
    socket.setdefaulttimeout(600)
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    llama_cpp = Path(args.llama_cpp).expanduser()
    token = load_token(args)
    jobs = load_jobs(args)
    if not jobs:
        raise RuntimeError("No jobs configured")
    if args.preflight_only:
        for job in jobs:
            preflight_job(job, token, llama_cpp, args)
        return
    for job in jobs:
        process_job(
            job=job,
            token=token,
            llama_cpp=llama_cpp,
            private=args.private,
            cleanup_after_upload=args.cleanup_after_upload,
            max_retries=args.max_upload_retries,
            args=args,
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[{now()}] FATAL {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        raise
