[Guide home](../../README.md) · [Training recipes](../README.md)

# Qwopus3.5 35B-A3B

**SFT · LoRA · Kaggle**

Follow a supervised fine-tune of a Qwen3.5 mixture-of-experts model. Use this recipe to inspect the data mixture and the model-specific choices in the 4-bit loading and adapter setup.

[Open in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) · [Notebook source](../Qwopus-3.5-35B-A3B-Kaggle.ipynb)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme-designs/annotated-edition/band-dark.svg">
  <img src="../../assets/readme-designs/annotated-edition/band-light.svg" alt="" width="760">
</picture>

## Before you run

Review the Kaggle accelerator and dataset permissions. Read the maximum sequence length in the loading cell, then check available memory for the full MoE checkpoint and your chosen batch settings. Set Kaggle Secrets for cells that use Hugging Face or Weights & Biases.

## Read the workflow

1. **Read the loading and adapter cells together.** Identify 4-bit loading, gradient checkpointing, and the modules selected for adaptation.
2. **Inspect each input dataset.** Follow the mixing strategy in the notebook and check how the tokenizer renders conversations from each source.
3. **Check supervised tokens.** Read the response-only mask and inspect a formatted sample from each source before training.

## Field note

> **Compare token lengths as well as counts.** After applying the chat template, check lengths by data source. A small number of long conversations can consume a large part of the run’s token budget.

## Artifacts and next steps

Read the notebook’s local adapter save and merged 16-bit export cells. For a second view of response-only training, see the [Qwen3.5 Neo 9B guide](./qwen35-9b-neo.md).
