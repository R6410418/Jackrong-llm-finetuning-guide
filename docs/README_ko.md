<div align="center">

# Jackrong LLM Fine-Tuning Guide

초보자와 개발자를 위한 오픈소스 LLM 파인튜닝, 데이터 증류, 강화학습, 로컬 배포 지식 베이스입니다.

🌐 **Languages:** [English](../README.md) | [中文](README_zh.md) | 한국어 | [日本語](README_ja.md)

🤗 **Hugging Face:** [Jackrong](https://huggingface.co/Jackrong)

🌐 **제품 웹사이트:** [Qwopus3.6 모델과 파인튜닝 가이드 보기 →](https://r6410418.github.io/Jackrong-llm-finetuning-guide/)

<br>

[![Unsloth](https://img.shields.io/badge/Powered%20by-Unsloth-8A2BE2?style=flat-square)](https://github.com/unslothai/unsloth)
[![Google Colab](https://img.shields.io/badge/Environment-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Model%20Hub-Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![LoRA PEFT](https://img.shields.io/badge/Technique-LoRA%20%2F%20PEFT-007EC6?style=flat-square)](#)
[![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-brightgreen?style=flat-square)](#)

</div>

---

이 저장소는 재현 가능한 training pipelines, SFT와 RL workflows(GRPO 및 GSPO 포함), 데이터 준비와 distillation recipes, 16-bit export와 GGUF deployment, agent-ready Qwen MTP GGUF conversion tools를 한곳에서 찾을 수 있도록 구성한 교육용 resource portal입니다.

## 📚 목차

- [🚀 시작하기](#-시작하기)
- [🗺️ 리포지토리 맵](#️-리포지토리-맵)
- [🏋️ 트레이닝 레시피](#️-트레이닝-레시피)
- [✅ 지원되는 워크플로우](#-지원되는-워크플로우)
- [🛣️ 모델 지원 로드맵](#️-모델-지원-로드맵)
- [⚙️ Qwen MTP GGUF Conversion Skill](#️-qwen-mtp-gguf-conversion-skill)
- [📘 가이드와 리포트](#-가이드와-리포트)
- [🧠 고품질 데이터셋 카탈로그](#-고품질-데이터셋-카탈로그)
- [🤝 오픈소스 약속](#-오픈소스-약속)
- [📚 인용](#-인용)

## 🚀 시작하기

| 하고 싶은 일 | 추천 항목 |
|---|---|
| 브라우저에서 첫 fine-tuning 실행 | [Training recipe catalog 열기](../train_code/) |
| Qwopus3.6 27B GSPO tutorial 실행 | [GSPO Python tutorial 열기](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| training data 준비 또는 distillation | [Data-processing recipes 보기](../data_processing_code/) |
| reasoning, coding, conversation datasets 찾기 | [Dataset catalog 열기](../High-fidelity%20Dataset/) |
| Qwen model을 MTP-enabled GGUF로 변환 | [Qwen MTP GGUF Skill 열기](../qwen-mtp-gguf/) |
| 긴 beginner guides와 reports 읽기 | [PDF guide library 열기](../guidePDF/) |
| 반복 가능한 Codex workflows 자동화 | [Codex Goal templates 열기](../codex-goals/) |

## 🗺️ 리포지토리 맵

| 리소스 | 포함 내용 | 항목 |
|---|---|---|
| 🏋️ Training Recipes | SFT, GRPO, GSPO notebooks와 Python tutorials | [열기](../train_code/) |
| 🧪 Data Processing | Distillation, preprocessing, cleaning, filtering, sampling workflows | [열기](../data_processing_code/) |
| 🧠 Dataset Catalog | Curated high-fidelity datasets와 download helpers | [열기](../High-fidelity%20Dataset/) |
| ⚙️ Qwen MTP GGUF Skill | MTP extraction, injection, conversion, validation, quantization, upload pipeline | [열기](../qwen-mtp-gguf/) |
| 📘 Guides and Reports | Long-form PDF tutorials와 technical reports | [열기](../guidePDF/) |
| 🌐 Multilingual Docs | Korean, Chinese, Japanese landing pages와 documentation index | [열기](README.md) |
| 🤖 Codex Goal Templates | RL training, MTP GGUF conversion, repository maintenance용 editable templates | [열기](../codex-goals/) |

## 🏋️ 트레이닝 레시피

| 모델 | 방법 | 환경 | 빠른 실행 |
|---|---|---|---|
| [Qwopus3.8 27B](../train_code/guides/qwen38-27b-colab.md) | SFT | Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.8-27B-Colab.ipynb) |
| Qwopus3.5 27B | SFT | Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| Qwopus3.6 27B | GSPO | Python script | [![Python Code](https://img.shields.io/badge/Code-Python-3776AB?style=flat-square&logo=python&logoColor=white)](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| Qwen3.5 9B | SFT | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| Qwopus3.5 35B | SFT | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| Llama3.2-R1 3B | GRPO | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

전체 목록은 [train_code/README.md](../train_code/README.md)를 참고하세요.

## ✅ 지원되는 워크플로우

| 워크플로우 | 상태 | 문서 |
|---|---|---|
| LoRA / QLoRA 기반 SFT | ✅ Released | [Training recipes](../train_code/) |
| GRPO reinforcement learning | ✅ Released | [Training recipes](../train_code/) |
| GSPO reinforcement learning | ✅ Released | [Qwopus3.6 27B GSPO tutorial](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| Dataset distillation and preprocessing | ✅ Released | [Data-processing recipes](../data_processing_code/) |
| LoRA adapter save and merged 16-bit export | ✅ Released | [Training recipes](../train_code/) |
| GGUF quantization | ✅ Released | [Training recipes](../train_code/) |
| Qwen MTP GGUF conversion | ✅ Released | [MTP conversion skill](../qwen-mtp-gguf/) |

## 🛣️ 모델 지원 로드맵

공개된 RL recipe는 모델과 목표에 따라 GRPO 또는 GSPO를 사용합니다.

| 모델 패밀리 | SFT 지원 | RL 지원 |
|---|---:|---:|
| Qwen 3.5 | ✅ Released | Scheduled |
| Qwen 3.6 | ✅ Released | ✅ Released |
| Qwen 3 | Scheduled | Scheduled |
| Llama3.2-R1 3B | ✅ Included | ✅ Released |
| Llama 3.1 / 3.3 | Scheduled | Scheduled |

## ⚙️ Qwen MTP GGUF Conversion Skill

[`qwen-mtp-gguf`](../qwen-mtp-gguf/) subproject는 Qwen-family MTP / nextn GGUF release workflow를 지원합니다. Disk, RAM, tooling, token access, compatibility preflight를 수행하고, compatible MTP tensors를 추출 및 주입한 뒤 llama.cpp로 변환하고 smoke test, quantization, safer upload/resume workflow를 제공합니다.

[🚀 MTP Skill 열기](../qwen-mtp-gguf/) · [📖 Pipeline Guide 읽기](../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md) · [🤖 Agent Usage Guide 읽기](../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md)

## 📘 가이드와 리포트

긴 PDF 문서는 [guide and technical report library](../guidePDF/README.md)에 정리되어 있습니다.

| 가이드 | 주제 | 파일 |
|---|---|---|
| Qwopus3.5 27B Colab complete guide | 초보자를 위한 end-to-end fine-tuning walkthrough | [PDF](../guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf) |
| Qwopus GLM 18B technical report | Model design과 training notes | [PDF](../guidePDF/Qwopus-GLM-18B-Technical-Report.pdf) |

## 🧠 고품질 데이터셋 카탈로그

이 저장소에는 reasoning, mathematics, coding, instruction following, conversation, domain-specific distillation을 위한 24개의 curated high-fidelity datasets가 포함되어 있습니다. 전체 [dataset catalog](../High-fidelity%20Dataset/README.md)를 보거나 [`download_datasets.py`](../download_datasets.py)로 로컬 학습용 데이터를 일괄 다운로드할 수 있습니다.

## 🤝 오픈소스 약속

이 프로젝트는 공개된 fine-tuned models의 training source code와 documentation을 가능한 한 열어 두어, 학습자가 workflows를 재현하고 검토하고 자신의 목적에 맞게 수정할 수 있도록 합니다. 더 긴 project philosophy와 original message to builders는 [PROJECT_PHILOSOPHY.md](PROJECT_PHILOSOPHY.md)에 보존되어 있습니다.

## 📚 인용

이 저장소가 학습이나 연구에 도움이 되었다면 아래와 같이 인용해 주세요.

```bibtex
@misc{jackrong-llm-finetuning,
  author = {Jackrong},
  title = {Jackrong LLM Fine-Tuning Guide: An Educational LLM Fine-Tuning Knowledge Base},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/R6410418/Jackrong-llm-finetuning-guide}}
}
```
