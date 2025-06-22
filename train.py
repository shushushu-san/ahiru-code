
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import (
    T5ForConditionalGeneration,
    T5Tokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq
)

def main():
    # 1. データの準備
    print("Loading and preparing data...")
    df = pd.read_csv('data/ahiru_corpus.csv')
    
    # 不完全な行を削除
    df.dropna(subset=['human_dialogue', 'duck_dialogue'], inplace=True)
    
    # データを訓練用と検証用に分割
    train_df, val_df = train_test_split(df, test_size=0.1, random_state=42)

    # 2. トークナイザーとモデルの準備
    model_name = 'sonoisa/t5-base-japanese' # 日本語T5モデル
    print(f"Loading tokenizer and model from {model_name}...")
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # 3. データセットの作成
    print("Creating datasets...")
    def preprocess_function(examples):
        # 入力と出力のテキストを準備
        inputs = ["アヒル語に翻訳: " + text for text in examples['human_dialogue']]
        targets = [text for text in examples['duck_dialogue']]
        
        # トークナイズ
        model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
        labels = tokenizer(text_target=targets, max_length=128, truncation=True, padding="max_length")
        
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    # DataFrameをHugging FaceのDataset形式に変換する必要がある
    # まずはPandasのまま前処理を適用
    # (注: 本来はdatasetsライブラリを使うのが効率的)
    
    # このスクリプトは雛形であり、datasetsライブラリの導入が必要です。
    # pip install datasets
    from datasets import Dataset
    train_dataset = Dataset.from_pandas(train_df)
    val_dataset = Dataset.from_pandas(val_df)

    tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)
    tokenized_val_dataset = val_dataset.map(preprocess_function, batched=True)

    # 4. トレーニングの設定
    print("Setting up training arguments...")
    training_args = Seq2SeqTrainingArguments(
        output_dir='./results',          # 結果の出力ディレクトリ
        num_train_epochs=3,              # トレーニングのエポック数
        per_device_train_batch_size=8,   # 訓練用バッチサイズ
        per_device_eval_batch_size=8,    # 評価用バッチサイズ
        warmup_steps=500,                # ウォームアップステップ数
        weight_decay=0.01,               # 重み減衰
        logging_dir='./logs',            # ログのディレクトリ
        logging_steps=10,
        evaluation_strategy="epoch",     # エポックごとに評価
        save_strategy="epoch",           # エポックごとに保存
        load_best_model_at_end=True,     # 最後に最高のモデルをロード
        report_to="none"                 # W&Bなどのレポーティングを無効化
    )

    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # 5. トレーナーの初期化とトレーニングの開始
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_val_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    print("Starting training...")
    trainer.train()

    # 6. モデルの保存
    print("Saving model...")
    model.save_pretrained('./ahiru_model')
    tokenizer.save_pretrained('./ahiru_model')
    print("Training finished and model saved in './ahiru_model'.")


if __name__ == "__main__":
    main()
