<div align="center">

# Jackrong LLM Fine-Tuning Guide

初心者と開発者のための、LLM ファインチューニング、データ蒸留、強化学習、ローカル展開を扱うオープンソース知識ベースです。

🌐 **Languages:** [English](../README.md) | [中文](README_zh.md) | [한국어](README_ko.md) | 日本語

🤗 **Hugging Face:** [Jackrong](https://huggingface.co/Jackrong)

🌐 **製品サイト：** [Qwopus3.6 モデルとファインチューニングガイドを見る →](https://r6410418.github.io/Jackrong-llm-finetuning-guide/)

<br>

[![Unsloth](https://img.shields.io/badge/Powered%20by-Unsloth-8A2BE2?style=flat-square)](https://github.com/unslothai/unsloth)
[![Google Colab](https://img.shields.io/badge/Environment-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Model%20Hub-Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![LoRA PEFT](https://img.shields.io/badge/Technique-LoRA%20%2F%20PEFT-007EC6?style=flat-square)](#)
[![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-brightgreen?style=flat-square)](#)

</div>

---

このリポジトリは、再現可能な training pipelines、SFT と RL workflows（GRPO と GSPO を含む）、データ準備と distillation recipes、16-bit export と GGUF deployment、agent-ready な Qwen MTP GGUF conversion tools をまとめた教育用 resource portal です。

## 📚 目次

- [🚀 はじめに](#-はじめに)
- [🗺️ リポジトリマップ](#️-リポジトリマップ)
- [🏋️ トレーニングレシピ](#️-トレーニングレシピ)
- [✅ 対応ワークフロー](#-対応ワークフロー)
- [🛣️ モデル対応ロードマップ](#️-モデル対応ロードマップ)
- [⚙️ Qwen MTP GGUF Conversion Skill](#️-qwen-mtp-gguf-conversion-skill)
- [📘 ガイドとレポート](#-ガイドとレポート)
- [🧠 高品質データセットカタログ](#-高品質データセットカタログ)
- [🤝 オープンソースへの約束](#-オープンソースへの約束)
- [📚 引用](#-引用)

## 🚀 はじめに

| やりたいこと | おすすめの入口 |
|---|---|
| ブラウザで初めて fine-tuning を実行する | [Training recipe catalog を開く](../train_code/) |
| Qwopus3.6 27B GSPO tutorial を実行する | [GSPO Python tutorial を開く](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| training data を準備または distillation する | [Data-processing recipes を見る](../data_processing_code/) |
| reasoning、coding、conversation datasets を探す | [Dataset catalog を開く](../High-fidelity%20Dataset/) |
| Qwen model を MTP-enabled GGUF に変換する | [Qwen MTP GGUF Skill を開く](../qwen-mtp-gguf/) |
| 長い beginner guides と reports を読む | [PDF guide library を開く](../guidePDF/) |
| 再利用できる Codex workflows を自動化する | [Codex Goal templates を開く](../codex-goals/) |

## 🗺️ リポジトリマップ

| リソース | 内容 | 入口 |
|---|---|---|
| 🏋️ Training Recipes | SFT、GRPO、GSPO notebooks と Python tutorials | [開く](../train_code/) |
| 🧪 Data Processing | Distillation、preprocessing、cleaning、filtering、sampling workflows | [開く](../data_processing_code/) |
| 🧠 Dataset Catalog | Curated high-fidelity datasets と download helpers | [開く](../High-fidelity%20Dataset/) |
| ⚙️ Qwen MTP GGUF Skill | MTP extraction、injection、conversion、validation、quantization、upload pipeline | [開く](../qwen-mtp-gguf/) |
| 📘 Guides and Reports | Long-form PDF tutorials と technical reports | [開く](../guidePDF/) |
| 🌐 Multilingual Docs | Japanese、Chinese、Korean landing pages と documentation index | [開く](README.md) |
| 🤖 Codex Goal Templates | RL training、MTP GGUF conversion、repository maintenance 用 editable templates | [開く](../codex-goals/) |

## 🏋️ トレーニングレシピ

| モデル | 方法 | 環境 | クイック実行 |
|---|---|---|---|
| [Qwopus3.8 27B](../train_code/guides/qwen38-27b-colab.md) | SFT | Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.8-27B-Colab.ipynb) |
| Qwopus3.5 27B | SFT | Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| Qwopus3.6 27B | GSPO | Python script | [![Python Code](https://img.shields.io/badge/Code-Python-3776AB?style=flat-square&logo=python&logoColor=white)](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| Qwen3.5 9B | SFT | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| Qwopus3.5 35B | SFT | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| Llama3.2-R1 3B | GRPO | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

完全な一覧は [train_code/README.md](../train_code/README.md) にあります。

## ✅ 対応ワークフロー

| ワークフロー | 状態 | ドキュメント |
|---|---|---|
| LoRA / QLoRA による SFT | ✅ Released | [Training recipes](../train_code/) |
| GRPO reinforcement learning | ✅ Released | [Training recipes](../train_code/) |
| GSPO reinforcement learning | ✅ Released | [Qwopus3.6 27B GSPO tutorial](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| Dataset distillation and preprocessing | ✅ Released | [Data-processing recipes](../data_processing_code/) |
| LoRA adapter save and merged 16-bit export | ✅ Released | [Training recipes](../train_code/) |
| GGUF quantization | ✅ Released | [Training recipes](../train_code/) |
| Qwen MTP GGUF conversion | ✅ Released | [MTP conversion skill](../qwen-mtp-gguf/) |

## 🛣️ モデル対応ロードマップ

公開済みの RL recipe は、モデルと目的に応じて GRPO または GSPO を使用します。

| モデルファミリー | SFT 対応 | RL 対応 |
|---|---:|---:|
| Qwen 3.5 | ✅ Released | Scheduled |
| Qwen 3.6 | ✅ Released | ✅ Released |
| Qwen 3 | Scheduled | Scheduled |
| Llama3.2-R1 3B | ✅ Included | ✅ Released |
| Llama 3.1 / 3.3 | Scheduled | Scheduled |

## ⚙️ Qwen MTP GGUF Conversion Skill

[`qwen-mtp-gguf`](../qwen-mtp-gguf/) subproject は Qwen-family MTP / nextn GGUF release workflow をサポートします。Disk、RAM、tooling、token access、compatibility preflight を行い、compatible MTP tensors を抽出・注入し、llama.cpp で変換し、smoke test、quantization、より安全な upload/resume workflow を提供します。

[🚀 MTP Skill を開く](../qwen-mtp-gguf/) · [📖 Pipeline Guide を読む](../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md) · [🤖 Agent Usage Guide を読む](../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md)

## 📘 ガイドとレポート

長い PDF は [guide and technical report library](../guidePDF/README.md) に整理されています。

| ガイド | トピック | ファイル |
|---|---|---|
| Qwopus3.5 27B Colab complete guide | 初心者向け end-to-end fine-tuning walkthrough | [PDF](../guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf) |
| Qwopus GLM 18B technical report | Model design と training notes | [PDF](../guidePDF/Qwopus-GLM-18B-Technical-Report.pdf) |

## 🧠 高品質データセットカタログ

このリポジトリには、reasoning、mathematics、coding、instruction following、conversation、domain-specific distillation 向けの 24 個の curated high-fidelity datasets があります。完全な [dataset catalog](../High-fidelity%20Dataset/README.md) を見るか、[`download_datasets.py`](../download_datasets.py) でローカルトレーニング用に一括ダウンロードできます。

## 🤝 オープンソースへの約束

このプロジェクトは、公開済み fine-tuned models の training source code と documentation をできるだけ開き、学習者が workflows を再現、確認、改造できるようにします。より長い project philosophy と original message to builders は [PROJECT_PHILOSOPHY.md](PROJECT_PHILOSOPHY.md) に保存されています。

## 📚 引用

このリポジトリが学習や研究に役立った場合は、以下の形式での引用をご検討ください。

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
