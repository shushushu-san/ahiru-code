import pandas as pd
import numpy as np

class DuckTranslator:
    def __init__(self, file_path='data/duck_language.csv', short_file_path='data/duck_language_short.csv', long_file_path='data/duck_language_long.csv', neutral_file_path='data/duck_language_neutral.csv'):
        """
        アヒル語のデータをCSVから読み込む
        """
        df_list = []
        for path in [file_path, short_file_path, long_file_path, neutral_file_path]:
            try:
                df = pd.read_csv(path)
                # 'text'列があったら'response'列にリネームする
                if 'text' in df.columns:
                    df = df.rename(columns={'text': 'response'})
                df_list.append(df)
            except FileNotFoundError:
                print(f"エラー: {path} が見つかりません。")

        if df_list:
            self.df = pd.concat(df_list, ignore_index=True)
            # VADスコアをNumpy配列に変換しておく
            self.vad_vectors = self.df[['v', 'a', 'd']].values
        else:
            self.df = pd.DataFrame(columns=['response', 'v', 'a', 'd'])
            self.vad_vectors = np.empty((0, 3))

    def translate_vad(self, vad_scores, top_n=25):
        """
        VADスコアに基づいて、最も近いアヒル語を確率的に選択して返します。
        距離が近いものほど選ばれやすくなります。

        Args:
            vad_scores (dict): {'v': float, 'a': float, 'd': float} の形式の辞書
            top_n (int): 候補とする上位N件の数

        Returns:
            str: 選択されたアヒル語
        """
        if self.df.empty:
            return "グワー… (データがないグワ…)"

        # 入力されたVADスコアをNumpy配列に変換
        input_vector = np.array([vad_scores['v'], vad_scores['a'], vad_scores['d']])

        # 全てのアヒル語のVADベクトルとのユークリッド距離を計算
        distances = np.linalg.norm(self.vad_vectors - input_vector, axis=1)

        # 距離が近い上位N件のインデックスを取得
        # Nがデータフレームの行数より大きい場合は、全行を対象にする
        num_candidates = min(top_n, len(self.df))
        candidate_indices = np.argsort(distances)[:num_candidates]

        # 候補が1つしかない、または完全に一致する候補がある場合は、それをそのまま返す
        if num_candidates <= 1 or distances[candidate_indices[0]] < 1e-6:
            return self.df.loc[candidate_indices[0], 'response']

        # 候補の距離を取得
        candidate_distances = distances[candidate_indices]

        # 距離から重みを計算 (距離が小さいほど重みが大きくなる)
        # 非常に小さい値を足して、ゼロ除算を避ける
        weights = 1.0 / (candidate_distances + 1e-6)

        # 重みを正規化して確率分布を作成
        probabilities = weights / np.sum(weights)

        # 確率分布に基づいて候補を1つ選択
        chosen_index = np.random.choice(candidate_indices, p=probabilities)

        # 選択された応答を返す
        return self.df.loc[chosen_index, 'response']
