# Model Adaptation Handbook

A practical guide to distillation, supervised and reward-based training, and local deployment for open language models.

<p>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme-designs/annotated-edition/masthead-dark.svg">
    <img src="./assets/readme-designs/annotated-edition/masthead-light.svg" alt="Qwopus wordmark with an eight-branch motif and fine editorial rules" width="720">
  </picture>
</p>

<a><img src="./assets/readme-designs/badges/qwen.svg" alt="Model · Qwen" width="93" height="20"></a> [![Unsloth](./assets/readme-designs/badges/unsloth.svg)](https://github.com/unslothai/unsloth)
[![Google Colab](./assets/readme-designs/badges/google-colab.svg)](https://colab.research.google.com/)
[![PyTorch](./assets/readme-designs/badges/pytorch.svg)](https://pytorch.org/)
[![Hugging Face](./assets/readme-designs/badges/hugging-face.svg)](https://huggingface.co/)
[![LoRA / PEFT](./assets/readme-designs/badges/lora-peft.svg)](./train_code/README.md#supervised-fine-tuning-sft)
[![Beginner Friendly](./assets/readme-designs/badges/beginner-friendly.svg)](./train_code/guides/qwopus35-27b-colab.md)

[Training catalog](./train_code/README.md) · [Model releases](#model-releases) · [Resources](#resources) · [Project website](https://r6410418.github.io/Jackrong-llm-finetuning-guide/) · [Hugging Face](https://huggingface.co/Jackrong)

English · [中文](./docs/README_zh.md) · [한국어](./docs/README_ko.md) · [日本語](./docs/README_ja.md)

## Training recipes

Each guide follows the published notebook or script through setup, data, training, and export.

| Recipe guide | Method | Environment | Focus | Quick setup |
|---|---|---|---|---|
| [Qwopus3.5 27B](./train_code/guides/qwopus35-27b-colab.md) | SFT | Colab | An end-to-end LoRA example with a companion PDF | [![Open in Colab](./assets/readme-designs/badges/open-in-colab.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| [Qwopus3.6 27B](./train_code/guides/qwopus36-27b-gspo.md) | GSPO-style RL | Python | Inspect the dataset schema, reward tests, and export paths | [![Python script](./assets/readme-designs/badges/python.svg)](./train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) |
| [Qwen3.5 Neo 9B](./train_code/guides/qwen35-9b-neo.md) | SFT | Kaggle | Normalize reasoning records and train on assistant responses | [![Open in Kaggle](./assets/readme-designs/badges/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| [Qwopus3.5 35B-A3B](./train_code/guides/qwopus35-35b-a3b.md) | SFT | Kaggle | Mix datasets and adapt a mixture-of-experts model | [![Open in Kaggle](./assets/readme-designs/badges/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| [Llama3.2-R1 3B](./train_code/guides/llama32-3b-grpo.md) | Cold-start SFT + GRPO | Kaggle | Follow the handoff from supervised training to rewards | [![Open in Kaggle](./assets/readme-designs/badges/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

**Workflow** · [Prepare the data](./data_processing_code/README.md) → [Choose a training recipe](./train_code/README.md) → [Review export and deployment](./train_code/README.md#export-and-deployment-notes)

## Model releases

| Model | Availability | Artifacts |
|---|---|---|
| DeepSeek-V4-Pro-Qwen3.5-9B | Public · reasoning distillation | [Model card](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B) · [MTP GGUF](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF) |
| Qwopus3.8-27B-Coder-Flash | Public · coding and tool use | [Model card](https://huggingface.co/Jackrong/Qwopus3.8-27B-Coder-Flash) · [GGUF](https://huggingface.co/Jackrong/Qwopus3.8-27B-Coder-Flash-GGUF) |
| DeepSeek-V4.1-Flash distillation | In preparation | Recipe and release details pending |
| Qwopus-9B-Coder-Flash-RL-V2 | In preparation | Standalone GB10 training environment planned |

The [training catalog](./train_code/README.md#planned-recipes) reserves space for Qwopus3.8 scripts and the forthcoming distillation and RL workflows.

## Field notes

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/readme-designs/personal-field-notes/notebook-dark.svg">
  <img src="./assets/readme-designs/personal-field-notes/notebook-light.svg" alt="Qwopus and the name Jackrong on ruled notebook paper" width="760">
</picture>

Jackrong started this guide from the questions that come with a first fine-tune. Each recipe points out a decision worth inspecting in the source, from chat formatting to reward behavior and export. [Project philosophy](./docs/PROJECT_PHILOSOPHY.md)

## Resources

| Resource | Start here |
|---|---|
| [Data processing and distillation](./data_processing_code/README.md) | [DeepSeek V4 API distillation notebook](./data_processing_code/DeepSeek-v4-API-distill.ipynb) |
| [High-Fidelity Dataset Catalog](./High-fidelity%20Dataset/README.md) | Reasoning, code, and conversation datasets · [Download utility](./download_datasets.py) |
| [Guides and technical reports](./guidePDF/README.md) | [Colab fine-tuning guide](./guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf) · [Qwopus GLM 18B report](./guidePDF/Qwopus-GLM-18B-Technical-Report.pdf) |
| [Qwen MTP GGUF toolkit](./qwen-mtp-gguf/README.md) | [Conversion pipeline](./qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md) · [Agent usage](./qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md) |
| [Codex goal templates](./codex-goals/README.md) | Reusable training, conversion, and repository workflows |
| [Documentation index](./docs/README.md) | Translations, project notes, and maintenance |

## Citation

```bibtex
@misc{jackrong-llm-finetuning,
  author = {Jackrong},
  title = {Jackrong LLM Fine-Tuning Guide: An Educational LLM Fine-Tuning Knowledge Base},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/R6410418/Jackrong-llm-finetuning-guide}}
}
```

[Apache-2.0 license](./LICENSE) · The MTP toolkit and linked models and datasets carry their own terms.
