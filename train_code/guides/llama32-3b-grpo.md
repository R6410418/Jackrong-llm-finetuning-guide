[Guide home](../../README.md) · [Training recipes](../README.md)

# Llama3.2-R1 3B

**Cold-start SFT + GRPO · LoRA · Kaggle**

This notebook starts from Llama-3.2-3B-Instruct and teaches the handoff from a supervised cold start to reward-based training on math prompts.

[Open in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) · [Notebook source](../Llama-3.2-3B-R1-Zero-GRPO.ipynb)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme-designs/annotated-edition/band-dark.svg">
  <img src="../../assets/readme-designs/annotated-edition/band-light.svg" alt="" width="760">
</picture>

## Before you run

Select a GPU runtime and inspect the install and model load cells. Check access to both datasets and review the completion length and number of generations in the GRPO configuration.

## Read the workflow

1. **Establish the answer format with SFT.** Follow how `OpenMathReasoning-mini` examples become conversations. The cold-start stage teaches the model the response format used later by the rewards.
2. **Read the transition section.** Find where the notebook switches to prompts and reference answers from `DAPO-Math-17k-Processed`.
3. **Inspect the sampled completions.** Review the reward functions and the `GRPOTrainer` setup. Compare completions against their reference answers before increasing generation count.

## Field note

> **Keep a sample at the handoff.** Read one completion after SFT and compare it with a GRPO sample from the same prompt. Check where the final answer lands and which part the reward reads.

## Artifacts and next steps

The final cells include merged 16-bit and GGUF export examples. To compare the reward setup with a sequence-level RL workflow, read the [Qwopus3.6 27B guide](./qwopus36-27b-gspo.md).
