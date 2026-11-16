<div align="center">

# Jackrong LLM Fine-Tuning Guide

面向初学者与开发者的端到端开源 LLM 微调、数据蒸馏、强化学习与本地部署知识库。

🌐 **Languages:** [English](../README.md) | 中文 | [한국어](README_ko.md) | [日本語](README_ja.md)

🤗 **Hugging Face:** [Jackrong](https://huggingface.co/Jackrong)

🌐 **产品网站：** [探索 Qwopus3.6 模型与微调教程 →](https://r6410418.github.io/Jackrong-llm-finetuning-guide/)

<br>

[![Unsloth](https://img.shields.io/badge/Powered%20by-Unsloth-8A2BE2?style=flat-square)](https://github.com/unslothai/unsloth)
[![Google Colab](https://img.shields.io/badge/Environment-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Model%20Hub-Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![LoRA PEFT](https://img.shields.io/badge/Technique-LoRA%20%2F%20PEFT-007EC6?style=flat-square)](#)
[![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-brightgreen?style=flat-square)](#)

</div>

---

这个仓库正在扩展为面向学习者和开发者的资源门户：你可以在这里找到可复现训练管线、SFT 与 RL（包括 GRPO 和 GSPO）工作流、数据准备与蒸馏配方、16-bit 导出与 GGUF 部署流程，以及面向 agent 的 Qwen MTP GGUF 转换工具。

## 📚 目录

- [🚀 从这里开始](#-从这里开始)
- [🗺️ 仓库地图](#️-仓库地图)
- [🏋️ 训练配方](#️-训练配方)
- [✅ 已支持工作流](#-已支持工作流)
- [🛣️ 模型支持路线图](#️-模型支持路线图)
- [⚙️ Qwen MTP GGUF 转换 Skill](#️-qwen-mtp-gguf-转换-skill)
- [📘 指南与报告](#-指南与报告)
- [🧠 高保真数据集目录](#-高保真数据集目录)
- [🤝 开源承诺](#-开源承诺)
- [📚 引用](#-引用)

## 🚀 从这里开始

| 我想要... | 推荐入口 |
|---|---|
| 在浏览器中完成第一次微调 | [打开训练配方目录](../train_code/) |
| 运行 Qwopus3.6 27B GSPO 教程 | [打开 GSPO Python 教程](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| 准备或蒸馏训练数据 | [浏览数据处理配方](../data_processing_code/) |
| 查找推理、代码和对话数据集 | [打开数据集目录](../High-fidelity%20Dataset/) |
| 将 Qwen 模型转换为 MTP-enabled GGUF | [打开 Qwen MTP GGUF Skill](../qwen-mtp-gguf/) |
| 阅读完整入门指南和报告 | [打开 PDF 指南库](../guidePDF/) |
| 自动化可复用的 Codex 工作流 | [打开 Codex Goal 模板](../codex-goals/) |

## 🗺️ 仓库地图

| 资源 | 内容 | 入口 |
|---|---|---|
| 🏋️ 训练配方 | SFT、GRPO、GSPO notebook 和 Python 教程 | [打开](../train_code/) |
| 🧪 数据处理 | 蒸馏、预处理、清洗、过滤与采样工作流 | [打开](../data_processing_code/) |
| 🧠 数据集目录 | 高保真数据集与批量下载工具 | [打开](../High-fidelity%20Dataset/) |
| ⚙️ Qwen MTP GGUF Skill | MTP 提取、注入、转换、验证、量化与发布流程 | [打开](../qwen-mtp-gguf/) |
| 📘 指南与报告 | 长篇 PDF 教程和技术报告 | [打开](../guidePDF/) |
| 🌐 多语言文档 | 中文、韩文、日文 landing page 与文档索引 | [打开](README.md) |
| 🤖 Codex Goal 模板 | RL 训练、MTP GGUF 转换和仓库维护的可编辑模板 | [打开](../codex-goals/) |

## 🏋️ 训练配方

| 模型 | 方法 | 环境 | 快速启动 |
|---|---|---|---|
| [Qwopus3.8 27B](../train_code/guides/qwen38-27b-colab.md) | SFT | Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.8-27B-Colab.ipynb) |
| Qwopus3.5 27B | SFT | Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| Qwopus3.6 27B | GSPO | Python script | [![Python Code](https://img.shields.io/badge/Code-Python-3776AB?style=flat-square&logo=python&logoColor=white)](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| Qwen3.5 9B | SFT | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| Qwopus3.5 35B | SFT | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| Llama3.2-R1 3B | GRPO | Kaggle | [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

完整列表见 [train_code/README.md](../train_code/README.md)。

## ✅ 已支持工作流

| 工作流 | 状态 | 文档 |
|---|---|---|
| LoRA / QLoRA SFT | ✅ 已发布 | [训练配方](../train_code/) |
| GRPO 强化学习 | ✅ 已发布 | [训练配方](../train_code/) |
| GSPO 强化学习 | ✅ 已发布 | [Qwopus3.6 27B GSPO 教程](../train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| 数据蒸馏与预处理 | ✅ 已发布 | [数据处理配方](../data_processing_code/) |
| LoRA adapter 保存与 merged 16-bit 导出 | ✅ 已发布 | [训练配方](../train_code/) |
| GGUF 量化 | ✅ 已发布 | [训练配方](../train_code/) |
| Qwen MTP GGUF 转换 | ✅ 已发布 | [MTP 转换 Skill](../qwen-mtp-gguf/) |

## 🛣️ 模型支持路线图

已发布的 RL 配方会根据模型和训练目标使用 GRPO 或 GSPO。

| 模型家族 | SFT 支持 | RL 支持 |
|---|---:|---:|
| Qwen 3.5 | ✅ 已发布 | 已排期 |
| Qwen 3.6 | ✅ 已发布 | ✅ 已发布 |
| Qwen 3 | 已排期 | 已排期 |
| Llama3.2-R1 3B | ✅ 已包含 | ✅ 已发布 |
| Llama 3.1 / 3.3 | 已排期 | 已排期 |

## ⚙️ Qwen MTP GGUF 转换 Skill

[`qwen-mtp-gguf`](../qwen-mtp-gguf/) 子项目支持 Qwen-family MTP / nextn GGUF 发布工作流。它会执行磁盘、内存、工具、token 权限和兼容性预检，提取并注入兼容的 MTP tensors，使用 llama.cpp 转换，执行 smoke test，量化输出，并支持更安全的上传与续传流程。

[🚀 打开 MTP Skill](../qwen-mtp-gguf/) · [📖 阅读 Pipeline Guide](../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md) · [🤖 阅读 Agent Usage Guide](../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md)

## 📘 指南与报告

长篇 PDF 收录在 [指南与技术报告库](../guidePDF/README.md)。

| 指南 | 主题 | 文件 |
|---|---|---|
| Qwopus3.5 27B Colab 完整指南 | 面向初学者的端到端微调 walkthrough | [PDF](../guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf) |
| Qwopus GLM 18B 技术报告 | 模型设计与训练说明 | [PDF](../guidePDF/Qwopus-GLM-18B-Technical-Report.pdf) |

## 🧠 高保真数据集目录

仓库包含 24 个高保真数据集，覆盖推理、数学、代码、指令跟随、多轮对话和领域数据。浏览完整 [数据集目录](../High-fidelity%20Dataset/README.md)，或使用 [`download_datasets.py`](../download_datasets.py) 批量下载到本地训练环境。

## 🤝 开源承诺

本项目会尽量让已发布微调模型对应的训练源码和说明保持开放，方便学习者复现、审阅和改造工作流。更长的项目理念与原始“给建设者的一封信”保存在 [PROJECT_PHILOSOPHY.md](PROJECT_PHILOSOPHY.md)。

## 📚 引用

如果这个仓库对你的学习或研究有帮助，请考虑引用：

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
