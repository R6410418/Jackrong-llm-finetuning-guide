[Guide home](../../README.md) · [Training recipes](../README.md)

# Qwopus3.8 27B

**SFT · 4-bit QLoRA · Google Colab**

Follow a supervised fine-tuning run with [`unsloth/Qwen3.8-27B`](https://huggingface.co/unsloth/Qwen3.8-27B). The notebook uses the model's chat template with adjustable reasoning effort, trains on assistant responses, and saves a Qwopus3.8 adapter.

[Open in Colab](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.8-27B-Colab.ipynb) · [Notebook source](../Qwen3.8-27B-Colab.ipynb)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme-designs/annotated-edition/band-dark.svg">
  <img src="../../assets/readme-designs/annotated-edition/band-light.svg" alt="" width="760">
</picture>

## Before you run

Select an A100-class CUDA GPU and add `WANDB_API_KEY` to Colab Secrets for training logs. Add `HF_TOKEN` if you plan to upload either export. The notebook caps training examples at 8,192 tokens.

## Read the workflow

1. **Load the base and add LoRA.** Load the 27B base in 4-bit with Unsloth and attach adapters to the language layers.
2. **Prepare the conversations.** Sample [DeepSeek-V4-Pro-Distilled-200K](https://huggingface.co/datasets/Jackrong/DeepSeek-V4-Pro-Distilled-200K) (Math and STEM) and [Claude-opus-4.7-TraceInversion-5000x](https://huggingface.co/datasets/Jackrong/Claude-opus-4.7-TraceInversion-5000x). The Qwopus3.8-27B-Coder-Flash training mix was assembled locally from many datasets. These two public datasets demonstrate preprocessing in Colab. You can substitute your own SFT datasets for other training goals.
3. **Apply the native template.** Give the tokenizer the trace as `reasoning_content` and the final answer as `content`. The template adds the thinking tags and accepts `low`, `medium`, or `xhigh` for reasoning effort.
4. **Filter and inspect.** Drop rows over the token cap, then preview a formatted example before training.

## Field note

> **Look at one formatted row first.** The response mask starts after the assistant's opening `<think>` tag, so the reasoning text and final answer contribute to training.

## Artifacts and next steps

The notebook saves checkpoints in `Qwopus3.8-27B-checkpoints` on Google Drive and writes the adapter and tokenizer to `Qwopus3.8-27B-LoRA` in the Colab runtime. The optional export cells upload `Qwopus3.8-27B-merged-16bit` or `Qwopus3.8-27B-GGUF`.
