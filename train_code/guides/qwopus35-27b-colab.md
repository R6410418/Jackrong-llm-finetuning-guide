[Guide home](../../README.md) · [Training recipes](../README.md)

# Qwopus3.5 27B

**SFT · LoRA · Google Colab**

Follow one supervised fine-tuning run from formatted conversations to a saved adapter. The notebook uses a Qwen3.5-27B base and shows the data, training, and export stages together.

[Open in Colab](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) · [Notebook source](../Qwopus3-5-27b-Colab.ipynb) · [Complete PDF guide](../../guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme-designs/annotated-edition/band-dark.svg">
  <img src="../../assets/readme-designs/annotated-edition/band-light.svg" alt="" width="760">
</picture>

## Before you run

Select a GPU runtime and read the setup cells in order. The notebook installs the training libraries and reads Hugging Face and Weights & Biases credentials from Colab Secrets for cells that use those services. Review the model context length and your runtime’s memory before loading the checkpoint.

## Read the workflow

1. **Load the base and add LoRA.** Identify the 4-bit loading configuration and the parameters assigned to the adapter.
2. **Prepare the conversations.** Follow the dataset loading and chat-template cells. Inspect a formatted example with both user and assistant turns.
3. **Check the training labels.** The notebook uses `train_on_responses_only` with the SFT trainer. Inspect the assistant boundary before starting the run.
4. **Read the save cells.** Follow local adapter saving, then review the separate merged 16-bit export cell if you need a standalone checkpoint.

## Field note

> **Look at one formatted row first.** A role boundary that differs from the response mask can leave the wrong tokens supervised. Decode a sample and check where the assistant response begins.

## Artifacts and next steps

The local save example writes the LoRA adapter and tokenizer to `qwen_lora`. The [companion PDF](../../guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf) goes deeper into setup and hyperparameters. For the reward-based workflow, continue to the [Qwopus3.6 27B guide](./qwopus36-27b-gspo.md).
