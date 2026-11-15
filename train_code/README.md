[← Guide home](../README.md)

# Training recipes

Choose by method and environment. The field guides explain where to begin and what to inspect before running each recipe.

## Supervised fine-tuning (SFT)

| Field guide | Environment | Source |
|---|---|---|
| [Qwopus3.5 27B](./guides/qwopus35-27b-colab.md) | Google Colab | [Notebook](./Qwopus3-5-27b-Colab.ipynb) · [Complete PDF guide](../guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf) |
| [Qwen3.5 Neo 9B](./guides/qwen35-9b-neo.md) | Kaggle | [Notebook](./Qwen3.5-9B-Neo-Kaggle.ipynb) |
| [Qwopus3.5 35B-A3B](./guides/qwopus35-35b-a3b.md) | Kaggle | [Notebook](./Qwopus-3.5-35B-A3B-Kaggle.ipynb) |

## Reinforcement learning (GRPO / GSPO)

| Field guide | Environment | Source |
|---|---|---|
| [Qwopus3.6 27B · GSPO-style](./guides/qwopus36-27b-gspo.md) | Python | [Training script](./Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) · [Technical notes](./Qwopus3.6-27B-GSPO/README.md) |
| [Llama3.2-R1 3B · cold-start SFT + GRPO](./guides/llama32-3b-grpo.md) | Kaggle | [Notebook](./Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

## Planned recipes

| Entry | Planned material |
|---|---|
| Qwopus3.8 series | Training scripts and field guides · [Coder-Flash model card](https://huggingface.co/Jackrong/Qwopus3.8-27B-Coder-Flash) |
| DeepSeek-V4-Pro-Qwen3.5-9B | Distillation and training write-up · [Model card](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B) |
| DeepSeek-V4.1-Flash distillation | Distillation recipe and release notes |
| Qwopus-9B-Coder-Flash-RL-V2 | RL recipe and a standalone GB10 training environment |

## Export and deployment notes

| Artifact | Reference |
|---|---|
| LoRA adapter | Save and reload cells in the individual notebooks, or the [GSPO adaptation guide](./guides/qwopus36-27b-gspo.md#artifacts-and-next-steps) |
| Merged 16-bit checkpoint | [GSPO merge notes](./Qwopus3.6-27B-GSPO/README.md#merge-and-save-16-bit-model-locally) |
| GGUF and optional vision projector | [GSPO export notes](./Qwopus3.6-27B-GSPO/README.md#export-gguf-q8_0) · [Projector notes](./Qwopus3.6-27B-GSPO/README.md#multimodal-projector-mmproj) · [Qwen MTP workflow](../qwen-mtp-gguf/README.md) |

## Add a recipe

Place the notebook or script under `train_code/` and add its field guide under `train_code/guides/`. Document the environment, dataset schema, a small validation step, and the expected export artifacts. Include a public or synthetic sample when a script needs one. [Repository maintenance guide](../docs/MAINTAINING_THE_KNOWLEDGE_BASE.md)
