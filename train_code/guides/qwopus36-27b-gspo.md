[Guide home](../../README.md) · [Training recipes](../README.md)

# Qwopus3.6 27B

**GSPO-style RL · LoRA · Python**

Read a reward-based post-training script for `Jackrong/Qwopus3.6-27B-v2`. The public tutorial includes data conversion, three reward functions, adapter saving, and export options.

[Training script](../Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py) · [Technical notes](../Qwopus3.6-27B-GSPO/README.md) · [Requirements](../Qwopus3.6-27B-GSPO/requirements-gspo.txt)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme-designs/annotated-edition/band-dark.svg">
  <img src="../../assets/readme-designs/annotated-edition/band-light.svg" alt="" width="760">
</picture>

## Before you run

Use the [environment setup notes](../Qwopus3.6-27B-GSPO/ENVIRONMENT_SETUP.txt) when preparing a CUDA-compatible Python environment. The reward loop samples multiple completions per prompt. Review generation count and total context against available GPU memory before training.

From the script directory, inspect how the bundled [synthetic rows](../Qwopus3.6-27B-GSPO/examples/sample_dataset_format.jsonl) are converted and run the built-in reward examples.

```bash
python qwopus3_6_27b_gspo_training.py dry-run-data
python qwopus3_6_27b_gspo_training.py test-rewards
```

## Read the workflow

1. **Convert answer-only rows.** Follow how prompt or message records become training prompts with an `expected_answer`. The loader skips rows containing tool definitions or lacking an expected answer.
2. **Inspect the three rewards.** Read how formatting, malformed output, and correctness are evaluated. Look up the answer normalization before adapting the verifier to a new domain.
3. **Read the trainer configuration.** The script uses TRL’s `GRPOTrainer` with sequence-level importance sampling, truncated-completion masking, and two generations by default. Find the run and resume commands in the [technical notes](../Qwopus3.6-27B-GSPO/README.md#train-from-scratch).

## Field note

> **Probe the reward boundary.** Try a correct answer with broken tags and a well-formatted answer that is wrong. Inspect the three scores separately so you can see which behavior each signal rewards.

## Artifacts and next steps

Adapter export, merged 16-bit export, and GGUF each have their own settings in the script. Follow the [GGUF export](../Qwopus3.6-27B-GSPO/README.md#export-gguf-q8_0) and [vision projector](../Qwopus3.6-27B-GSPO/README.md#multimodal-projector-mmproj) notes for deployment. See the [Qwen MTP toolkit](../../qwen-mtp-gguf/README.md) for compatible checkpoints.
