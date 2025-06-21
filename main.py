import sys
from vad_analyzer import get_vad_scores
from duck_translator import DuckTranslator

# アヒル語翻訳機を準備
translator = DuckTranslator()

def main():
    """AIとの対話を実行する"""
    print("アヒルAI (「さようなら」で終了)")
    print("（初回実行時はモデルのダウンロードに時間がかかることがあります）")

    # Windows環境での文字化け対策
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except TypeError:
            # reconfigureが利用できない古いPython環境向けのフォールバック
            import codecs
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

    while True:
        try:
            user_input = input("あなた: ")
        except UnicodeDecodeError:
            print("アヒル: ??? (文字がうまく読み取れないグワ…)")
            continue

        if not user_input:
            continue
        if user_input.lower() in ["さようなら", "exit", "quit"]:
            print("アヒル: グワッ… (さびしそうに去っていく)")
            break

        # 感情をVADスコアとして分析
        vad_scores = get_vad_scores(user_input)

        # VADスコアに基づいてアヒル語に翻訳
        duck_response = translator.translate_vad(vad_scores)

        print(f"アヒル: {duck_response}")
        # デバッグ用にVADスコアも表示
        print(f"（V: {vad_scores['v']:.2f}, A: {vad_scores['a']:.2f}, D: {vad_scores['d']:.2f}）")

if __name__ == "__main__":
    main()
