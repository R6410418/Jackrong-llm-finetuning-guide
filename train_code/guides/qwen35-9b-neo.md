[Guide home](../../README.md) · [Training recipes](../README.md)

# Qwen3.5 Neo 9B

**SFT · LoRA · Kaggle**

Use this notebook to study how example conversations from different sources become one assistant-supervised training set. The notebook loads a Qwen3.5 9B base with 4-bit weights.

[Open in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) · [Notebook source](../Qwen3.5-9B-Neo-Kaggle.ipynb)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme-designs/annotated-edition/band-dark.svg">
  <img src="../../assets/readme-designs/annotated-edition/band-light.svg" alt="" width="760">
</picture>

## Before you run

Select a GPU accelerator, read the package install and model load cells, and check dataset access. Configure the notebook’s Hugging Face and Weights & Biases secrets in Kaggle for the cells that need them.

## Read the workflow

1. **Normalize the assistant turn.** Trace how `reasoning_content` becomes a `<think>` block followed by the answer, including the empty-block case.
2. **Assemble the training mix.** See where the notebook formats two source datasets, concatenates them, and shuffles with a fixed seed. Inspect both sources before changing the ratio.
3. **Verify response masking.** The SFT trainer is wrapped with `train_on_responses_only`. Check the role markers against the rendered conversation before training.

## Field note

> **Compare the empty and nonempty reasoning cases.** Read one row of each after formatting. Check that the answer follows the closing `</think>` tag inside the assistant turn.

## Artifacts and next steps

The notebook saves an adapter and tokenizer in `qwen_lora` and includes a merged 16-bit export example. Compare how the [35B-A3B recipe](./qwopus35-35b-a3b.md) handles its dataset mix.
