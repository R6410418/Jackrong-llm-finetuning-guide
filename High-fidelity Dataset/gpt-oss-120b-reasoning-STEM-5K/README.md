---
license: apache-2.0
task_categories:
- question-answering
- text-generation
- translation
- summarization
language:
- en
pretty_name: gpt-oss-120b-reasoning-STEM-10K
size_categories:
- 1K<n<10K
---




# GPT-OSS-120B-Distilled-Reasoning-STEM Dataset

## 1) Dataset Overview

*   **Data Source Model**: `gpt-oss-120b-high`
*   **Task Type**: **STEM Reasoning and Problem Solving** (Science, Technology, Engineering & Mathematics)
*   **Data Format**: `JSON Lines 
*   **Fields**: `generator`, `category`, `input`, `CoT_Native——reasoning`, `answer`
    (Consistent with the math dataset, splitting the original 'output' into 'reasoning' and 'answer' for COT/SFT scenarios.)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/EW5fKpnazIIw8SEd6hnaW.png)

## 2) Design Goals (Motivation)

This dataset targets **comprehensive STEM reasoning**: covering concept understanding, **multi-step deduction**, and **formula/theorem application** across **Mathematics, Physics, Chemistry, Computer Science, Engineering, and Life Sciences**. Unlike datasets that only provide the final answer, this dataset clearly distinguishes between "**reasoning chain (reasoning)**" and "**answer (answer)**", facilitating:

*   Training/fine-tuning models with **reasoning capabilities** (**COT/SFT**).
*   Evaluating **dual-dimensional metrics** of "**correct process/correct answer**".
*   **Flexible extraction** for different downstream tasks (QA only, reasoning only, full dataset).

Regarding transparency and responsible use information that should be included in data cards, I follow industry best practices such as **Dataset Cards / Datasheets for Datasets / Dataset Nutrition Label**.

## 3) Data Source & Distillation

*   **Generation Model**: **gpt-oss-120b** (high reasoning configuration), generating complete reasoning processes and final answers.
*   **Prompt Coverage**: **Multiple-choice questions, short-answer questions, calculation/proofs, concept questions**, etc., across **STEM** fields.
*   **Cleaning and Structuring**:
    *   Splitting the model's full output into `reasoning` and `answer` segments, preserving "**native reasoning text**";
    *   Filtering out **empty answers, truncated/overflowing outputs**, and **clearly incomplete samples**;
    *   **Deduplication** primarily based on the `input` prompt;
    *   **Standardizing fields and labels** to ensure **downstream usability**.

## 4) Schema & Format

**One sample per line (JSONL)**:

```json
{
 "Generator": "gpt-oss-120b",
 "Category": "stem",
 "Input": "Prompt/Question Text",
 "CoT_Native——reasoning": "Complete multi-step thinking process (native reasoning chain)",
 "Answer": "Final answer text (decoupled from reasoning)"
}
```
## 5) Quality & Known Limitations

*   **Generative Bias**: Samples originate from the same large model family, potentially introducing **stylistic and knowledge biases**; it is recommended to **mix with other sources** for training to enhance **robustness**.
*   **Reasoning Chain Noise**: Despite cleaning, individual samples may still exhibit **verbosity/repetition** or **slight inconsistencies** with the answer; it is recommended to perform **secondary audits** before training or use **heuristic rules** for further segmentation and annotation.
*   **Subject Coverage**: The distribution across STEM sub-fields is **not perfectly balanced**; samples for **long-tail subjects** (e.g., Materials Science/Fluid Dynamics) are **relatively fewer**.
*   **Responsible Use**: Should **not be used for exam cheating** or generating **misleading scientific conclusions**; for **high-risk scenarios** involving Medicine/Chemistry/Engineering, etc., it is crucial to include **expert review** or **human verification** steps.

## 6) License & Intended Use

*   **License**: **CC-BY-4.0** 
*   **Primary Use**: For **COT/SFT training**, **reasoning evaluation**, **data analysis**, and **visualization teaching** in **academic/industrial scenarios**.
*   **Out-of-Scope**: It is **not recommended** to directly use reasoning chains "**without human review**" for **high-risk decisions** such as **clinical diagnosis**, **engineering safety reviews**, etc.

## 7) Acknowledgements
*  The construction of this dataset is based on the generation capabilities of gpt-oss-120b and the optimized design of STEM reasoning templates.
*  **Seed Questions**: Derived in part from nvidia/Nemotron-Post-Training-Dataset-v1.











