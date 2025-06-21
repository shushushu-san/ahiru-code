# あひるAI

## 開発方針

このプロジェクトは、ユーザーの日本語入力から感情を推定し、それに応じたアヒル語を返すAIを作成することを目的としています。

当初は単純な感情ラベル（例: `positive`, `negative`, `neutral`）による分類を検討していましたが、より繊細で多次元的な感情表現を実現するため、**VADモデル** を採用する方針に転換しました。

VADモデルを用いることで、感情をより細かく捉え、多様なアヒル語の鳴き声や行動を生成することを目指します。

## VADモデルについて

VADモデルは、感情を以下の3つの次元で評価するモデルです。

- **Valence (V)**: 感情の快・不快の度合い（ポジティブかネガティブか）
- **Arousal (A)**: 感情の興奮・覚醒の度合い（昂っているか落ち着いているか）
- **Dominance (D)**: 感情の優位性・支配性の度合い（強気か弱気か）

これらの3つのスコアを組み合わせることで、喜び、悲しみ、怒り、驚きといった単純な分類では表現しきれない、複雑な感情の状態を数値として捉えることができます。

本AIでは、Hugging Faceで公開されている日本語の事前学習済みモデル `koheiduck/bert-japanese-finetuned-sentiment` を利用して、入力されたテキストからVADスコアを算出しています。

## 実行方法

1. 必要なライブラリをインストールします。

   ```shell
   pip install -r requirements.txt
   ```

   (注: `requirements.txt` がまだない場合は、以下のコマンドで主要なライブラリをインストールしてください)

   ```shell
   pip install torch transformers pandas fugashi ipadic unidic-lite sentencepiece
   ```

2. `main.py` を実行します。

   ```shell
   python main.py
   ```

3. コンソールに日本語で話しかけると、アヒルAIがアヒル語で応答します。終了するには `exit` と入力してください。

## ファイル構造

```text
ahiru-ai/
│
├── main.py                 # AIのメインプログラム
├── vad_analyzer.py         # VADスコアを分析・算出するモジュール
├── duck_translator.py      # VADスコアをアヒル語に翻訳するモジュール
│
├── data/
│   ├── duck_language.csv     # アヒル語の表現と対応するVADスコアのデータ
│   └── human_language.csv    # (現在は未使用) 人間の言葉のサンプルデータ
│
└── README.md               # このファイル
```
