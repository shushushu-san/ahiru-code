import csv
import os
import requests  # Ollamaとの通信に使用
import json      # Ollamaからの応答をパースするために使用
import re        # 応答テキストの解析をより堅牢にするために使用

# --- Ollama API設定 ---
OLLAMA_API_URL = "http://localhost:11434/api/generate"
# ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
# ★ ここに、あなたがOllamaで利用したいモデル名を入力してください ★
# 例: "llama3", "gemma:2b", "command-r"など
OLLAMA_MODEL = "hf.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf:Q4_K_M"  # ← ★★★ 書き換えてください ★★★
# ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

def call_ollama_api(theme: str, num_examples: int = 2):
    """
    ローカルのOllama APIを呼び出し、指定されたテーマで対話ペアを生成します。
    """
    print(f"--- Ollama(モデル: {OLLAMA_MODEL})を呼び出し中 (テーマ: {theme}) ---")

    prompt = f'''あなたは賢いアヒルのキャラクターです。
人間の言葉に対して、アヒルがどう反応するかを生成するタスクを実行します。
応答は「鳴き声（行動や感情）」の形式でお願いします。

テーマ：「{theme}」

上記のテーマに沿った「人間の言葉」と「アヒルの応答」のペアを{num_examples}個、以下の形式で厳密に出力してください。

human: (ここに人間の言葉)
duck: (ここにアヒルの応答)

human: (ここに人間の言葉)
duck: (ここにアヒルの応答)
'''

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()  # エラーがあれば例外を発生させる

        response_text = response.json().get("response", "")
        return parse_llm_response(response_text)

    except requests.exceptions.RequestException as e:
        print(f"\n[エラー] Ollama APIへの接続に失敗しました。")
        print("Ollamaアプリケーションが起動していることを確認してください。")
        print(f"詳細: {e}")
        return []

def parse_llm_response(response_text: str):
    """
    LLMからの応答テキストを解析し、対話ペアの辞書のリストに変換します。
    """
    pairs = []
    # "human:" で分割して、各ペアを処理する
    human_sections = re.split(r'human:', response_text, flags=re.IGNORECASE)

    for section in human_sections:
        if not section.strip():
            continue

        # "duck:" で人間の言葉とアヒルの応答を分割
        duck_split = re.split(r'duck:', section, flags=re.IGNORECASE)
        if len(duck_split) == 2:
            human_text = duck_split[0].strip()
            duck_response = duck_split[1].strip()
            pairs.append({"human": human_text, "duck": duck_response})

    return pairs

def generate_new_data():
    """
    定義されたテーマに基づいて、Ollamaを呼び出し、新しい対話データを生成する。
    """
    # ここに生成したいテーマを追加していくだけで、データが自動生成される
    themes_to_generate = [
        "日常の挨拶",
        "面白いものを見つけた時",
        "慰めてほしい時",
        "くだらない冗談を言う",
        "応援してほしい時",
        "秘密を打ち明ける時",
        "感謝の気持ちを伝える",
        "失敗して謝る",
        "何かに怒っている",
        "突然の出来事に驚く",
        "とても嬉しいことがあった",
        "悲しい気持ちになっている",
        "一緒に何かをしようと誘う",
        "不思議なものについて質問する",
        "今日の天気について話す",
        "お腹が空いた、何か食べたい",
        "眠くて仕方がない",
        "困っていて助けを求めている",
        "体調が悪い時",
        "夢の話をする",
        "昔の思い出を語る",
        "好きな食べ物について",
        "嫌いな食べ物について",
        "趣味について話す",
        "仕事や勉強の愚痴",
        "恋愛相談",
        "怖い話をする",
        "感動した話をする",
        "旅行の計画を立てる",
        "欲しいものについて",
        "新しいことを始めた",
        "疲れている時",
        "のんびりしたい時",
        "季節のイベントについて（春）",
        "季節のイベントについて（夏）",
        "季節のイベントについて（秋）",
        "季節のイベントについて（冬）",
        "誕生日を祝う",
        "誰かを褒める",
        "考え事をしている",
        "何かを探している",
        "道を尋ねる",
        "スポーツの話題",
        "音楽の話題",
        "映画の話題",
        "読書の話題",
        "ゲームの話題",
        "ただ相槌を打ってほしい"
    ]

    all_new_pairs = []
    for theme in themes_to_generate:
        # 各テーマについて、2つの新しい対話ペアを生成
        generated_pairs = call_ollama_api(theme, num_examples=2)
        all_new_pairs.extend(generated_pairs)

    return all_new_pairs

def main():
    """
    データ生成を実行し、CSVファイルに追記するメイン関数
    """
    file_path = os.path.join('data', 'ahiru_corpus.csv')

    # 生成する新しいデータを取得
    data_to_add = generate_new_data()

    # 既存のデータを読み込み、重複をチェック
    existing_human_texts = set()
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            try:
                next(reader)  # ヘッダーをスキップ
            except StopIteration:
                pass  # ファイルが空の場合は何もしない
            for row in reader:
                if row:
                    existing_human_texts.add(row[0])
    except FileNotFoundError:
        # ファイルが存在しない場合は、ヘッダーを書き込む準備
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["human_text", "duck_response"])

    # 新しいデータだけをファイルに追記
    added_count = 0
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for pair in data_to_add:
            if pair["human"] not in existing_human_texts:
                writer.writerow([pair["human"], pair["duck"]])
                added_count += 1

    print(f"処理が完了しました。{added_count}件の新しいデータを {file_path} に追加しました。")

if __name__ == "__main__":
    main()
