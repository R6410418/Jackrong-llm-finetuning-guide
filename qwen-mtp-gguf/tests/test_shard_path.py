import sys
from pathlib import Path

import pytest
import torch
from safetensors.torch import save_file

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qwen_mtp_gguf_pipeline as pipe  # noqa: E402

KEY = "model.mtp.fc.weight"


@pytest.fixture
def opened(monkeypatch):
    calls = []
    real = pipe.safe_open

    def spy(path, *a, **kw):
        calls.append(str(path))
        return real(path, *a, **kw)

    monkeypatch.setattr(pipe, "safe_open", spy)
    return calls


@pytest.fixture
def outside(tmp_path):
    f = tmp_path / "outside" / "victim.safetensors"
    f.parent.mkdir()
    save_file({KEY: torch.full((2,), 42.0)}, str(f))
    return f


def bad_names(outside):
    return [
        str(outside),
        "../outside/victim.safetensors",
        "sub/../../outside/victim.safetensors",
        "C:\\x.safetensors",
        "..\\outside\\victim.safetensors",
        "",
        "model.bin",
        None,
    ]


def test_validate_rejects_escaping_names(tmp_path, outside, opened):
    model_dir = tmp_path / "model"
    model_dir.mkdir()
    for name in bad_names(outside):
        with pytest.raises(RuntimeError, match="Unsafe shard name|missing weight_map"):
            pipe.validate_indexed_tensors(model_dir, [KEY], {KEY: name})
    assert opened == []


def test_extract_rejects_escaping_names(tmp_path, outside, opened, monkeypatch):
    snap = tmp_path / "snap"
    snap.mkdir()
    monkeypatch.setattr(pipe, "snapshot_download", lambda **kw: str(snap))
    job = type("J", (), {"reusable_mtp_heads": [], "mtp_source_repo": "x/y"})()
    for name in bad_names(outside):
        monkeypatch.setattr(pipe, "source_mtp_shards", lambda *a, n=name: ([KEY], [n]))
        with pytest.raises(RuntimeError):
            pipe.extract_mtp_heads(job, None, tmp_path / "out.safetensors", tmp_path / "log")
    assert opened == []
    assert not (tmp_path / "out.safetensors").exists()


def test_source_mtp_shards_rejects(tmp_path, outside, monkeypatch):
    idx = tmp_path / "model.safetensors.index.json"
    idx.write_text('{"weight_map": {"%s": "%s"}}' % (KEY, str(outside)))
    monkeypatch.setattr(pipe, "hf_hub_download", lambda **kw: str(idx))
    with pytest.raises(RuntimeError, match="Unsafe shard name"):
        pipe.source_mtp_shards("x/y", None)


def test_valid_shard_and_symlink_allowed(tmp_path, opened):
    model_dir = tmp_path / "model"
    model_dir.mkdir()
    blob = tmp_path / "blobs" / "abc"
    blob.parent.mkdir()
    save_file({KEY: torch.ones(2)}, str(blob))
    (model_dir / "model-00001.safetensors").symlink_to(blob)
    pipe.validate_indexed_tensors(model_dir, [KEY], {KEY: "model-00001.safetensors"})
    assert len(opened) == 1
