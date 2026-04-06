<div align="center">

# Jackrong-llm-finetuning-guide 🌌
**초보자와 개발자를 위한 교육용 엔드투엔드 LLM 파인튜닝 파이프라인**

🌐 **언어 선택:**  [🇬🇧 **English**](../README.md) ｜ [🇨🇳 中文](./README_zh.md) ｜ 🇰🇷 **한국어** ｜ [🇯🇵 日本語](./README_ja.md)

🤗 **HuggingFace:** [Jackrong](https://huggingface.co/Jackrong)

<br>

[![Unsloth](https://img.shields.io/badge/Powered%20by-Unsloth-8A2BE2?style=flat-square)](https://github.com/unslothai/unsloth)
[![Google Colab](https://img.shields.io/badge/Environment-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Model%20Hub-Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![LoRA PEFT](https://img.shields.io/badge/Technique-LoRA%20%2F%20PEFT-007EC6?style=flat-square)](#)
[![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-brightgreen?style=flat-square)](#)

</div>

---

## 📑 요약

초보자와 개발자를 위해 특별히 설계된 대형 언어 모델(LLM) 파인튜닝 교육용 리포지토리입니다. 이 프로젝트는 자세한 이론적 설명, 강력한 데이터 처리 워크플로우, 재현 가능한 학습 파이프라인(지도 미세 조정 SFT 및 향후 강화 학습 RL 구현 포함)과 실질적인 배포 전략을 제공합니다. 작성자가 오픈소스로 제공하는 모델의 전체 학습 코드를 이 저장소에서 완벽히 확인할 수 있습니다.

<div align="center">
  <img width="100%" alt="프로젝트 개요" src="https://github.com/user-attachments/assets/67dff316-e77e-4909-a338-56caeb6583b4" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 20px 0;"/>
</div>

---

## 🏛️ 프로젝트 소개

이 저장소는 **"0에서 1까지"**를 배울 수 있는 학습 플랫폼으로 구축되었습니다. 기술적 배경지식이 전혀 없든, 숙련된 개발자이든 관계없이 대규모 언어 모델의 전체 수명 주기를 안내하는 재현 가능한 엔드투엔드 가이드를 찾을 수 있습니다. Google 계정을 등록하고 Colab을 여는 간단한 시작 단계부터 모델을 특정 도메인 요구에 효율적으로 맞추는 방법까지 배우게 됩니다.

### ✨ 핵심 기능

| 항목 | 설명 |
| :--- | :--- |
| 🛤️ **0에서 1까지의 학습 경로** | 웹 브라우저와 무료 클라우드 환경만 있으면 시작할 수 있는 최기초 단계부터의 단계별 가이드. |
| 🔄 **다양한 학습 워크플로우** | SFT(지도 미세 조정)를 비롯해 RL(강화 학습) 등의 고급 패러다임을 위한 코드베이스 및 기초 설정. |
| ⚡ **효율적인 리소스 엔지니어링** | Unsloth 및 4-bit 양자화 도구를 활용하여 단일 GPU(예: 기본 Google Colab)의 한계 내에서 대규모 학습 실행. |
| 📦 **엔드투엔드 배포** | 다중 소스 데이터의 정규화부터 LoRA 어댑터 적용, 16-bit 병합형 배포, 로컬 구동을 위한 GGUF 양자화 아웃풋까지. |

---

## 💡 제작자의 메시지

> [!NOTE]
> *"초보자, 취미로 즐기는 분, AI에 호기심을 가진 모든 분들께: 이 길은 배울 수 있는 길입니다."*

이 문서의 목적은 단순히 단일 학습 실행에 대해 설명하는 것을 넘어 더 넓은 메시지를 전하는 데 있습니다. 파인튜닝, 사후 훈련, 심지어 промежут적인 스케일의 사전 훈련조차 **접근하기 불가능한 고도의 기술적 의식**이 아닙니다. 그것들은 배우고 재현하고 점진적으로 완벽해질 수 있는 **엔지니어링 프랙티스(공학적 관행)**입니다. 오픈소스 모델, 공개 데이터셋, 클라우드 컴퓨팅 플랫폼, 그리고 점차 성숙해지는 학습 도구 체인이 있다면 필요한 것은 Google 계정, 일반적인 노트북, 그리고 끊임없는 호기심뿐입니다.

마찬가지로 밑바닥부터 시작한 학습자로서, 저는 수많은 초보자들이 직면하게 되는 불확실성을 이해합니다. 환경 설정의 복잡성, 불투명한 하이퍼파라미터, 연산 자원에 대한 불안감 등은 종종 진입을 가로막는 첫 번째 장벽이 되곤 합니다. 그렇기 때문에 Unsloth와 같은 최적화 도구 체인이 중요합니다. 학습 효율과 자원 활용도를 높임으로써 대규모 모델 파인튜닝의 실질적인 진입 장벽을 대폭 낮추고, 과거엔 값비싼 하드웨어와 전문 경험이 필요했던 일들을 일반 개발자들도 일상적으로 시도하고 정복할 수 있는 일로 바꿔놓았습니다.

**이런 의미에서, 우리 모두는 거인의 어깨 위에 서서 모델을 이해하고 변형하며, 그것들에 새로운 능력을 부여할 기회를 가지고 있습니다.**

*처음부터 전문가인 사람은 없습니다. 하지만 모든 전문가는 용기를 내어 첫걸음을 내디뎠습니다.*

## 🚀 향후 모델 지원 및 로드맵

가까운 미래에 이 리포지토리는 최신 최고 성능의 오픈소스 모델 라인업에 대한 지원을 지속적으로 확장할 예정입니다. 곧 공개될 튜토리얼과 코드베이스는 **지도 미세 조정(SFT)**과 **강화 학습(RL - 특히 GRPO)** 파이프라인을 포괄적으로 다룹니다.

현재 계획된 모델 지원 매트릭스는 다음과 같습니다:

| 모델 라인업 | SFT 지원 | RL (GRPO) 지원 |
| :--- | :---: | :---: |
| **Qwen 3.5** | ✅ 출시됨 | 예정됨 |
| **Qwen 3** | 예정됨 | 예정됨 |
| **Llama** (3.1 / 3.2 / 3.3) | 예정됨 | 예정됨 |
| **Phi-4** | 예정됨 | 예정됨 |
| **Gemma 4** | 예정됨 | 예정됨 |
| **DeepSeek** | 예정됨 | 예정됨 |

---

## 📓 대화형 학습 노트북

아래는 모델 아키텍처별로 정리된 Colab 노트북입니다. 데이터 준비부터 학습, 추론까지의 전체 파이프라인을 브라우저에서 직접 실행할 수 있습니다. 모든 노트북은 저장소의 [`train_code`](../train_code/) 폴더에 저장되어 있습니다.

### 🌟 메인 노트북

| 🤖 모델 아키텍처 | 🛠️ 파이프라인 | 🚀 빠른 설정 (1-Click 실행) |
| :--- | :--- | :---: |
| **Qwopus3.5 (27B)** | SFT / LoRA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwen3.5 (9B)** | SFT / LoRA | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 (35B)** | SFT / LoRA | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |

---

## 📖 종합 모델 학습 가이드

Qwopus 3.5 파인튜닝 프로세스 전체(환경 설정, 데이터 준비 및 최적화 팁 포함)에 대한 자세한 단계별 PDF 설명을 보려면 최신 가이드를 참조하십시오.

> [!TIP]
> **🔗 [전체 가이드 다운로드: Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**

---

## 📚 고품질 증류 데이터셋

효과적인 모델 파인튜닝의 핵심 엔진은 고품질의 데이터입니다. 당사의 학습 코드와 병행하여, 이 워크스페이스는 모델의 추론, 프로그래밍 및 대화 기능을 강화하기 위해 특별히 수집되고 정제된 **24개의 선별된 고품질 증류 데이터셋**을 이용할 수 있도록 제공합니다.

이 데이터셋들은 주로 *DeepSeek-V3.2*, *Qwen3-235B*, *GLM-4.7*, 그리고 *GPT-OSS-120B*와 같은 최첨단 플래그십 모델들에서 증류되었으며, 향상된 생각의 사슬(CoT) 형식을 따르고 있습니다.

**포함된 주요 데이터 카테고리:**
*   🧠 **추론 및 CoT (Chain-of-Thought):** 단계별 논리 및 연역을 향상시키기 위해 설계된 `Jackrong/Qwen3.5-reasoning-700`, `Jackrong/Natural-Reasoning-gpt-oss-120B-S1`, `Jackrong/glm-4.7-multiturn-CoT`와 같은 데이터.
*   📐 **수학 및 STEM:** 특화된 도메인 지식을 갖춘 `DeepSeek-v3.1-reasoner-Distilled-math-samples` 및 `Jackrong/Qwen3-235B-A22B-Instruct-2507-Distilled-chat`.
*   💻 **코드 및 알고리즘:** 정규 알고리즘 생성과 알고리즘 테스트(Competitive Programming) 강화를 위한 `Competitive-Programming-python-blend` 및 `qwen3-coder-480b-distill-mini` 컬렉션.
*   💬 **지시 및 다중 턴 대화:** 인간 정렬(human alignment), IELTS 쓰기 피드백, 그리고 자연스럽고 안정적인 대화 흐름 개선에 초점을 맞춘 `Jackrong/LogicMind-Chat-Reasoning-SFT-300K`, `Chinese-Qwen3-235B-Thinking-2507-Distill-100k`, `ShareGPT-gpt-oss-120B-reasoning` 등의 자원.

*모든 데이터셋은 [HuggingFace Hub](https://huggingface.co/Jackrong)에서 무료로 공개되고 있습니다. 동봉된 `download_datasets.py` 스크립트를 사용하여 로컬 파인튜닝용 전체 데이터 세트를 일괄 다운로드할 수도 있습니다.*

---

## 🌍 오픈소스 선언 및 커뮤니티 영향

앞으로 제가 Hugging Face를 통해 공개하는 모든 미세 조정 모델의 전체 학습 소스 코드는 이 저장소에 완전한 오픈소스로 공개될 것입니다. 저의 목표는 출신 배경이나 자원에 구애받지 않고 누구나 이 스크립트를 자유롭게 다운로드하고 실행시키고 학습하여 자신만의 AI 역량을 구축할 수 있도록 돕는 것입니다.

커뮤니티의 아낌없는 성원에 깊이 감사드립니다. 최근 제가 Hugging Face에 공유한 Qwen3.5 파인튜닝 모델이 **백만 회 이상의 다운로드**에 도달했습니다. 이는 오픈 지식의 힘을 조용하지만 강력하게 증명하는 대목입니다. 이 완벽한 학습 파이프라인 구성이 더 많은 개발자들의 파인튜닝 여정에 영감을 줄 수 있기를 진심으로 바랍니다.

---

## 📝 인용

학습이나 연구에 이 저장소가 도움이 되었다면 아래와 같이 인용해 주세요.

```bibtex
@misc{jackrong-llm-finetuning,
  author = {Jackrong},
  title = {Jackrong-llm-finetuning-guide: An Educational LLM Fine-Tuning Pipeline},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Jackrong/Jackrong-llm-finetuning-guide}}
}
```
