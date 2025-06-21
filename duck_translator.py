import pandas as pd
import numpy as np

class DuckTranslator:
    def __init__(self, file_path='data/duck_language.csv'):
        """
        アヒル語のデータをCSVから読み込む
        """
        try:
            self.df = pd.read_csv(file_path)
            # VADスコアをNumpy配列に変換しておく
            self.vad_vectors = self.df[['v', 'a', 'd']].values
        except FileNotFoundError:
            print(f"エラー: {file_path} が見つかりません。")
            self.df = pd.DataFrame(columns=['response', 'v', 'a', 'd'])
            self.vad_vectors = np.empty((0, 3))

    def translate_vad(self, vad_scores):
        """
        VADスコアに基づいて、最も近いアヒル語を返します。

        Args:
            vad_scores (dict): {'v': float, 'a': float, 'd': float} の形式の辞書

        Returns:
            str: 最も近いアヒル語
        """
        if self.df.empty:
            return "グワー… (データがないグワ…)"

        # 入力されたVADスコアをNumpy配列に変換
        input_vector = np.array([vad_scores['v'], vad_scores['a'], vad_scores['d']])

        # 全てのアヒル語のVADベクトルとのユークリッド距離を計算
        distances = np.linalg.norm(self.vad_vectors - input_vector, axis=1)

        # 最も距離が近い応答のインデックスを取得
        closest_index = np.argmin(distances)

        # 最も近い応答を返す
        return self.df.loc[closest_index, 'response']
