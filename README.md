<div align="center">

# Jackrong-llm-finetuning-guide 🌌
**An Educational, End-to-End LLM Fine-Tuning Pipeline for Beginners and Developers**

🌐 **Select Language:**  🇬🇧 **English** ｜ [🇨🇳 中文](./docs/README_zh.md) ｜ [🇰🇷 한국어](./docs/README_ko.md) ｜ [🇯🇵 日本語](./docs/README_ja.md)

🤗 **HuggingFace:** [Jackrong](https://huggingface.co/Jackrong)

<br>

[![Unsloth](https://img.shields.io/badge/Powered%20by-Unsloth-8A2BE2?style=flat-square)](https://github.com/unslothai/unsloth)
[![Google Colab](https://img.shields.io/badge/Environment-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Model%20Hub-Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![LoRA PEFT](https://img.shields.io/badge/Technique-LoRA%20%2F%20PEFT-007EC6?style=flat-square)](#)
[![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-brightgreen?style=flat-square)](#)

</div>

---

## 📑 Abstract

An educational Large Language Model (LLM) fine-tuning repository designed for beginners and developers. This project provides detailed theoretical explanations, robust data processing workflows, reproducible training pipelines (including Supervised Fine-Tuning and future Reinforcement Learning implementations), and practical deployment strategies. The full training code for the author's open-source projects is fully accessible within this repository.

<div align="center">
  <img width="100%" alt="Project Overview" src="https://github.com/user-attachments/assets/67dff316-e77e-4909-a338-56caeb6583b4" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 20px 0;"/>
</div>

---

## 🏛️ About This Project

This repository is designed as a **"Zero to One"** learning platform. Whether you have zero technical background or are an experienced developer, you will find reproducible, end-to-end guides that walk you through the entire lifecycle of large language models. Starting from simply registering a Google account and opening Colab, you will learn how to efficiently adapt models to your specific domain needs.

### ✨ Key Features & Offerings

| Aspect | Description |
| :--- | :--- |
| 🛤️ **0-to-1 Learning Path** | Step-by-step guides starting from the absolute basics, requiring nothing more than a browser and a free cloud environment. |
| 🔄 **Diverse Training Workflows** | Codebases covering Supervised Fine-Tuning (SFT) and foundational setups for Reinforcement Learning (RL) and other advanced paradigms. |
| ⚡ **Resource-Efficient Engineering** | Leveraging tools like Unsloth and 4-bit quantization to run large-scale training within single-GPU constraints (e.g., standard Google Colab). |
| 📦 **End-to-End Delivery** | From multi-source data normalization to LoRA adaptation, merged 16-bit exports, and GGUF quantization for local deployment. |

---

## 💡 A Message to Builders

> [!NOTE]
> *"For beginners, hobbyists, and anyone curious about AI: this path is learnable."*

The purpose of this document is not only to describe one training run, but also to communicate a broader message: fine-tuning, post-training, and even moderate-scale pretraining are **not inaccessible technical rituals**. They are **engineering practices** that can be learned, reproduced, and gradually mastered. With open-source models, public datasets, cloud compute platforms, and an increasingly mature training toolchain, what you often need is simply a Google account, a regular laptop, and sustained curiosity.

As a learner who also started from zero, I understand the uncertainty many newcomers face: environment setup complexity, opaque hyperparameters, and anxiety about compute resources often become the first barrier to entry. This is exactly why optimization toolchains such as Unsloth matter: by improving training efficiency and resource utilization, they substantially lower the practical threshold for large-model fine-tuning, turning what once required expensive hardware and specialized experience into something ordinary developers can attempt and master.

**In that sense, we all have the opportunity to stand on the shoulders of giants, understand models, adapt models, and give them new capabilities.**

*No one starts as an expert. But every expert was once brave enough to begin.*

## 🚀 Upcoming Model Support & Roadmap

In the near future, this repository will continuously expand its support for the latest state-of-the-art open-source model families. The upcoming tutorials and codebases will comprehensively cover both **Supervised Fine-Tuning (SFT)** and **Reinforcement Learning (RL - specifically GRPO)** pipelines.

Below is the planned support matrix for upcoming model families:

| Model Family | SFT Support | RL (GRPO) Support |
| :--- | :---: | :---: |
| **Qwen 3.5** | ✅ Released | Scheduled |
| **Qwen 3** | Scheduled | Scheduled |
| **Llama** (3.1 / 3.2 / 3.3) | Scheduled | Scheduled |
| **Phi-4** | Scheduled | Scheduled |
| **Gemma 4** | Scheduled | Scheduled |
| **DeepSeek** | Scheduled | Scheduled |

---

## 📓 Interactive Training Notebooks

Below are the Colab notebooks, organized by model architecture. You can run the entire pipeline—from data preparation to training and inference—directly in your browser. All notebooks are available in the [`train_code`](./train_code/) repository folder.

### 🌟 Main Notebooks

| 🤖 Model Architecture | 🛠️ Pipeline | 🚀 Quick Setup (1-Click Run) |
| :--- | :--- | :---: |
| **Qwopus3.5 (27B)** | SFT / LoRA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwen3.5 (9B)** | SFT / LoRA | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 (35B)** | SFT / LoRA | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |

---

## 📖 Comprehensive Model Training Guide

For a detailed, step-by-step PDF walkthrough of the entire Qwopus 3.5 fine-tuning process—including environment setup, data preparation, and optimization tips—please refer to our latest guide:

> [!TIP]
> **🔗 [Download Complete Guide: Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**

---

## 📚 High-Fidelity Distillation Datasets

High-quality data is the engine of effective model adaptation. In parallel with our training code, this repository provides access to **24 curated, high-fidelity datasets** specifically collected and distilled to enhance model reasoning, coding, and conversational capabilities.

These datasets are primarily distilled from state-of-the-art flagship models (such as *DeepSeek-V3.2*, *Qwen3-235B*, *GLM-4.7*, and *GPT-OSS-120B*) and follow advanced Chain-of-Thought (CoT) formatting. 

**Key Dataset Categories Included:**
*   🧠 **Reasoning & CoT (Chain-of-Thought):** Datasets like `Jackrong/Qwen3.5-reasoning-700`, `Jackrong/Natural-Reasoning-gpt-oss-120B-S1`, and `Jackrong/glm-4.7-multiturn-CoT` designed to improve step-by-step logic and deduction.
*   📐 **Mathematics & STEM:** Specialized data such as `DeepSeek-v3.1-reasoner-Distilled-math-samples` and focused domain knowledge like `Jackrong/Qwen3-235B-A22B-Instruct-2507-Distilled-chat`.
*   💻 **Code & Algorithms:** Collections like `Competitive-Programming-python-blend` and `qwen3-coder-480b-distill-mini` to strengthen competitive programming and algorithmic generation.
*   💬 **Instruction & Multi-turn Chat:** Resources like `Jackrong/LogicMind-Chat-Reasoning-SFT-300K`, `Chinese-Qwen3-235B-Thinking-2507-Distill-100k`, and `ShareGPT-gpt-oss-120B-reasoning` focused on human alignment, IELTS writing feedback, and robust conversational flowing.

*All datasets are open-sourced on the [HuggingFace Hub](https://huggingface.co/Jackrong). You can also use the included `download_datasets.py` script to batch download the entire suite for local training.*

---

## 🌍 Open Source Commitment & Community Impact

Moving forward, the complete training source code for every fine-tuned model I release on Hugging Face will be fully open-sourced in this repository. My goal is to ensure that anyone—regardless of their background or resources—can freely download, execute, and learn from these scripts to build their own AI capabilities.

I am deeply grateful for the community's support. The Qwen3.5 fine-tunes I shared on Hugging Face have recently reached over a **million downloads**—a quiet reminder of the power of open knowledge. It is my sincere hope that making these full training pipelines publicly available will encourage more developers to start their own fine-tuning journeys.

---

## 📝 Citation

If you find this repository helpful in your learning or research, please consider citing it:

```bibtex
@misc{jackrong-llm-finetuning,
  author = {Jackrong},
  title = {Jackrong-llm-finetuning-guide: An Educational LLM Fine-Tuning Pipeline},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Jackrong/Jackrong-llm-finetuning-guide}}
}
```
