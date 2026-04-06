<div align="center">

# Jackrong-llm-finetuning-guide 🌌
**初心者と開発者のための教育用エンドツーエンド LLM ファインチューニング パイプライン**

🌐 **言語の選択:**  [🇬🇧 **English**](../README.md) ｜ [🇨🇳 中文](./README_zh.md) ｜ [🇰🇷 한국어](./README_ko.md) ｜ 🇯🇵 **日本語**

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

## 📑 概要

初心者と開発者のために設計された、大規模言語モデル（LLM）ファインチューニング教育用リポジトリです。このプロジェクトでは、詳細な理論的解説、堅牢なデータ処理ワークフロー、再現可能なトレーニングパイプライン（教師ありファインチューニング SFT および将来の強化学習 RL 実装を含む）、実用的なデプロイ戦略を提供します。また、開発者がオープンソース化するモデルの完全なトレーニングコードも、このリポジトリで全公開されています。

<div align="center">
  <img width="100%" alt="プロジェクトの概要" src="https://github.com/user-attachments/assets/67dff316-e77e-4909-a338-56caeb6583b4" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin: 20px 0;"/>
</div>

---

## 🏛️ このプロジェクトについて

このリポジトリは、**「ゼロからイチへ」**の学習プラットフォームとして設計されています。技術的なバックグラウンドが全くない方でも、熟練した開発者でも、大規模言語モデルのライフサイクル全体を体系的に学べるエンドツーエンドのガイドを用意しています。Googleアカウントを作成し、Colabを開くという最初のステップから、特定のドメインニーズにモデルを効率的に適合させる方法まで学習できます。

### ✨ 主な特徴

| 分野 | 説明 |
| :--- | :--- |
| 🛤️ **0から1への学習パス** | ブラウザと無料のクラウド環境のみで始められる、基礎からのステップバイステップガイド。 |
| 🔄 **多様なトレーニングワークフロー** | 教師あり学習（SFT）だけでなく、強化学習（RL）などの高度なパラダイムの基礎を含んだコードペース。 |
| ⚡ **リソース効率の高いエンジニアリング** | Unslothのようなツールや4ビット量子化を活用し、単一のGPU（標準的なGoogle Colab等）の制約下でも大規模モデルの学習を実行可能に。 |
| 📦 **エンドツーエンドの提供** | 多ソースデータの正規化から、LoRAアダプテーション、16ビットのエクスポート結合、およびローカル展開用のGGUF量子化まで。 |

---

## 💡 開発者へのメッセージ

> [!NOTE]
> *「初心者、趣味で開発する方、AIに好奇心を持つすべての人へ：この道は必ず学べるものです。」*

このドキュメントの目的は、単に一度のトレーニング結果を説明することではなく、より大きなメッセージを伝えることにあります。ファインチューニングやポストトレーニング、さらに中規模の事前学習でさえ、**決して手の届かない高度な技術的儀式**ではありません。それらは学んで再現し、徐々にマスターすることができる**エンジニアリングのプラクティス**です。オープンソースのモデル、公開データセット、クラウドコンピューティング基盤、そして成熟しつつあるトレーニングツールチェーンの存在により、あなたに必要なのはGoogleアカウント、普通のノートパソコン、そして持続する好奇心だけです。

私自身もゼロから始めた学習者であるからこそ、環境設定の複雑さ、難解なハイパーパラメータ、計算リソースへの不安など、初心者が直面する不確実性をよく理解しています。だからこそ、Unslothのような最適化ツールチェーンが重要なのです。学習効率とリソースの利用率を向上させることで、大規模モデルのファインチューニングのハードルを大幅に下げ、かつては高価なハードウェアや専門知識が必要だったものを、一般の開発者が日常的に試み、マスターできるように変えたのです。

**その意味で、私たちは皆、巨人の肩の上に立ち、モデルを理解し、適用し、全く新しい能力を与える機会を持っているのです。**

*最初から専門家である人はいません。しかし、すべての専門家はかつて勇敢に最初の一歩を踏み出しました。*

## 🚀 今後のモデルサポートとロードマップ

近い将来、本リポジトリは最新のトップレベルのオープンソースモデルへのサポートを拡大し続けます。近日公開のチュートリアルとコードベースは、**教師ありファインチューニング（SFT）**と**強化学習（RL - 特にGRPO）**のパイプラインを網羅的にカバーします。

今後公開されるモデルサポートの予定は以下の通りです：

| モデルファミリー | SFT サポート | RL (GRPO) サポート |
| :--- | :---: | :---: |
| **Qwen 3.5** | ✅ リリース済み | 予定 |
| **Qwen 3** | 予定 | 予定 |
| **Llama** (3.1 / 3.2 / 3.3) | 予定 | 予定 |
| **Phi-4** | 予定 | 予定 |
| **Gemma 4** | 予定 | 予定 |
| **DeepSeek** | 予定 | 予定 |

---

## 📓 インタラクティブなトレーニングノートブック

以下は、モデルアーキテクチャ別に整理された Colab ノートブックです。データ準備からトレーニング、推論に至るまでのパイプライン全体をブラウザで直接実行できます。すべてのノートブックは、リポジトリの [`train_code`](../train_code/) ディレクトリに保存されています。

### 🌟 メインノートブック

| 🤖 モデルアーキテクチャ | 🛠️ パイプライン | 🚀 クイックセットアップ (1-Click 実行) |
| :--- | :--- | :---: |
| **Qwopus3.5 (27B)** | SFT / LoRA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwen3.5 (9B)** | SFT / LoRA | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 (35B)** | SFT / LoRA | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |

---

## 📖 総合モデルトレーニングガイド

Kwopus 3.5 のファインチューニングプロセス全体（環境設定、データ準備、最適化のヒントを含む）の詳細なステップバイステップ PDF ウォークスルーについては、最新のガイドを参照してください。

> [!TIP]
> **🔗 [フルガイドをダウンロード: Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**

---

## 📚 高精度な蒸留データセット

効果的なモデルの適応には、高品質なデータが不可欠です。本リポジトリでは、トレーニングコードと並行して、推論、コーディング、および対話能力を最適化するために収集および「蒸留」された**厳選された24の高精度データセット**を利用することができます。

これらのデータセットは主に、*DeepSeek-V3.2*、*Qwen3-235B*、*GLM-4.7*、および*GPT-OSS-120B*などの最新フラグシップモデルから蒸留され、高度な思考の連鎖（CoT: Chain-of-Thought）形式を採用しています。

**含まれる主要なデータカテゴリ：**
*   🧠 **推論および CoT (思考の連鎖)：** 段階的な推論と論理的能力を強化するための `Jackrong/Qwen3.5-reasoning-700`、`Jackrong/Natural-Reasoning-gpt-oss-120B-S1`、および `Jackrong/glm-4.7-multiturn-CoT`。
*   📐 **数学および STEM：** 特殊なドメイン知識を持つ `DeepSeek-v3.1-reasoner-Distilled-math-samples` や `Jackrong/Qwen3-235B-A22B-Instruct-2507-Distilled-chat` などのデータ。
*   💻 **コードおよびアルゴリズム：** 競技プログラミングおよびアルゴリズム生成を強化するための `Competitive-Programming-python-blend` や `qwen3-coder-480b-distill-mini` のコレクション。
*   💬 **指示およびマルチターンチャット：** 人間との連携、IELTSライティングのフィードバック、堅牢な会話フローの改善に焦点を当てた `Jackrong/LogicMind-Chat-Reasoning-SFT-300K`、`Chinese-Qwen3-235B-Thinking-2507-Distill-100k` および `ShareGPT-gpt-oss-120B-reasoning` 等のリソース。

*すべてのデータセットは [HuggingFace Hub](https://huggingface.co/Jackrong) 上でオープンソース化されています。同封のローカルスクリプト (`download_datasets.py`) を実行することで、ローカルトレーニング用に一括ダウンロードすることもできます。*

---

## 🌍 オープンソースへの誓いとコミュニティへの貢献

今後、私がHugging Faceで公開するすべてのファインチューニングモデルの完全なトレーニングソースコードは、このリポジトリにすべてオープンソース化されます。私の目標は、背景やリソースに関係なく、誰もが自由にこれらをダウンロードし、実行し、学ぶことで、自らのAI機能を構築できるようにすることです。

コミュニティのサポートに深く感謝いたします。最近Hugging Faceで共有したQwen3.5のファインチューニングは**100万回以上のダウンロード**を達成しました。これはオープンな知識の力を証明するものです。この完全なトレーニング体験が公開されることで、より多くの開発者が自身のファインチューニングの旅に出るきっかけとなることを心から願っています。

---

## 📝 引用

学習や研究でこのリポジトリが役立った場合は、以下の方法での引用をご検討ください：

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
