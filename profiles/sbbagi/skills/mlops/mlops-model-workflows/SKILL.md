---
name: mlops-model-workflows
description: "Use when working with ML/LLM operations: Hugging Face Hub, local inference, vLLM serving, llama.cpp, evaluation harnesses, W&B tracking, model surgery, audio/image models."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [mlops, llm, inference, evaluation, huggingface, vllm, llama-cpp, wandb]
    related_skills: []
---

# MLOps Model Workflows

## Overview

This umbrella covers practical model operations: discovering/downloading/uploading artifacts, serving models, evaluating them, tracking experiments, and running specialized model workflows. Former packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- Searching, downloading, or uploading Hugging Face models/datasets.
- Running GGUF/local inference with llama.cpp or high-throughput serving with vLLM.
- Benchmarking models with lm-eval-harness or tracking with Weights & Biases.
- Running specialized model workflows such as AudioCraft, Segment Anything, or model refusal surgery.

## Workflow Map

1. **Artifact discovery**: identify model/dataset IDs, revisions, licenses, and hardware needs.
2. **Local/served inference**: choose llama.cpp for GGUF/local CPU/GPU workflows; choose vLLM for OpenAI-compatible high-throughput serving.
3. **Evaluation/tracking**: record exact model, dataset, prompt/template, metrics, and W&B run links where applicable.
4. **Specialized models**: verify dependencies, checkpoints, and sample outputs before reporting success.
5. **Safety and reproducibility**: preserve commands, seeds, versions, and generated artifacts.

## Source Packages

- `references/source-packages/huggingface-hub/`
- `references/source-packages/llama-cpp/`
- `references/source-packages/vllm/`
- `references/source-packages/lm-evaluation-harness/`
- `references/source-packages/weights-and-biases/`
- `references/source-packages/obliteratus/`
- `references/source-packages/audiocraft/`
- `references/source-packages/segment-anything/`

## Verification Checklist

- [ ] Model/artifact identifiers and revisions are recorded.
- [ ] Hardware and dependency assumptions are checked.
- [ ] Inference/evaluation commands actually run or blockers are stated.
- [ ] Output artifacts, metrics, or server health endpoints are verified.
