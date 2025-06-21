from transformers import pipeline, AutoTokenizer

# 1. Hugging Faceから日本語感情分析モデルのパイプラインをロード
model_name = "koheiduck/bert-japanese-finetuned-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
# 全てのスコアを返すように設定
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model=model_name,
    tokenizer=tokenizer,
    return_all_scores=True
)

def get_vad_scores(text: str) -> dict:
    """
    日本語テキストから感情を分析し、VADスコアに変換します。
    ポジティブとネガティブの両方のスコアを考慮して、より滑らかなVAD値を計算します。

    Args:
        text (str): 分析する日本語のテキスト

    Returns:
        dict: {'v': float, 'a': float, 'd': float} の形式のVADスコア
    """
    # モデルはテキストが空だとエラーを出すため、空の場合はニュートラルを返す
    if not text.strip():
        return {'v': 0.0, 'a': 0.0, 'd': 0.0}
        
    # モデルによる感情分類の実行
    # [[{'label': 'positive', 'score': ...}, {'label': 'negative', 'score': ...}]]
    # の形式で返ってくる
    results = sentiment_analyzer(text)

    # スコアを辞書に変換
    scores = {item['label'].lower(): item['score'] for item in results[0]}
    pos_score = scores.get('positive', 0.0)
    neg_score = scores.get('negative', 0.0)

    # VADスコアを計算
    # v (Valence): 快-不快。-1.0 (不快) ~ 1.0 (快)
    v = pos_score - neg_score

    # a (Arousal): 覚醒度。0.0 (穏やか) ~ 1.0 (興奮)
    # 感情の強さ(ポジティブかネガティブに振れている度合い)を覚醒度とする
    a = abs(v)

    # d (Dominance): 優位度。-0.5 (従属) ~ 0.5 (優位)
    # 快(v>0)なら優位、不快(v<0)なら従属とする簡易的なマッピング
    d = v * 0.5

    final_vad = {'v': v, 'a': a, 'd': d}

    return final_vad

# --- テスト実行 ---
if __name__ == '__main__':
    text1 = "今日はとても良い天気で、最高の気分です！"
    vad1 = get_vad_scores(text1)
    print(f"'{text1}' -> V: {vad1['v']:.2f}, A: {vad1['a']:.2f}, D: {vad1['d']:.2f}")

    text2 = "最悪の事態になってしまった。とても悲しい。"
    vad2 = get_vad_scores(text2)
    print(f"'{text2}' -> V: {vad2['v']:.2f}, A: {vad2['a']:.2f}, D: {vad2['d']:.2f}")

    text3 = "これはペンです。"
    vad3 = get_vad_scores(text3)
    print(f"'{text3}' -> V: {vad3['v']:.2f}, A: {vad3['a']:.2f}, D: {vad3['d']:.2f}")