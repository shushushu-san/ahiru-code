# AHIRU-CODE

## 概要

ユーザーが入力した日本語のテキストから感情を分析し、その感情にマッチしたアヒル語の鳴き声や行動を返します。

## 特徴

- **VADモデルによる感情分析**: 従来のポジティブ/ネガティブといった単純な感情分類ではなく、VAD（Valence-Arousal-Dominance）モデルを採用しています
  - **Valence (V)**: 快・不快の度合い
  - **Arousal (A)**: 興奮・覚醒の度合い
  - **Dominance (D)**: 優位・支配の度合い
- **多様なアヒル語表現**: 様々なな表現を可能にするため、複数のCSVファイルでコーパスを管理しています。これにより、繊細で豊かな感情表現が可能です。
- **確率的な応答選択**: VADスコアが完全に一致する表現だけでなく、スコアが近い表現も候補に含め、その距離に応じた確率で応答を選択します。これにより、毎回少しずつ異なる自然な応答が生成されます。

## 実行方法

1. 必要なライブラリをインストールします。

   ```shell
   pip install -r requirements.txt
   ```

   **PowerShellの場合の注意:** 初回実行時にスクリプトの実行が拒否された場合は、以下のコマンドを実行してください：

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **（オプション）どこからでも実行できるようにする設定:**

   **自動セットアップ（推奨）:**

   ```shell
   setup.bat
   ```

   **PowerShell実行ポリシーエラーが出る場合:**

   ```shell
   .\setup.ps1
   ```

   **PATH設定確認:**

   ```shell
   .\check_path.bat
   ```

   **手動でWindows環境変数を設定:**
   1. `Win + R` を押して `sysdm.cpl` を実行
   2. 「詳細設定」タブ → 「環境変数」をクリック
   3. ユーザー環境変数の「Path」を選択 → 「編集」
   4. 「新規」をクリックして、`ahiru-code`フォルダの絶対パスを追加
      例: `C:\Users\gents\1.University\Projects\Yukari_tech\ahiruAI\ahiru-code`
   5. 「OK」で保存し、新しいターミナルを開く

   **PowerShellで一時的に設定する場合:**

   ```powershell
   $env:PATH += ";C:\Users\gents\1.University\Projects\Yukari_tech\ahiruAI\ahiru-code"
   ```

3. プログラムを実行します。以下のいずれかの方法で実行できます：

   **方法1: 専用コマンド（推奨）**

   ```shell
   # PowerShellの場合
   .\ahiru
   
   # コマンドプロンプトの場合
   ahiru
   ```

   **方法2: Pythonスクリプトとして直接実行**

   ```shell
   python ahiru.py
   ```

   **方法3: メインファイルを直接実行**

   ```shell
   python main.py
   ```

4. コンソールに日本語で話しかけると、アヒルAIがアヒル語で応答します。終了するには `exit` または`さようなら`と入力してください。

## ファイル構造

```text
ahiru-code/
│
├── setup.bat               # PATH設定用セットアップスクリプト
├── setup.ps1               # PATH設定用セットアップスクリプト（PowerShell版）
├── check_path.bat          # PATH設定確認スクリプト
├── test_ahiru.ps1          # ahiruコマンドテストスクリプト
├── ahiru.cmd               # 統合実行スクリプト（推奨）
├── ahiru.py                # 実行用スクリプト
├── ahiru.bat               # Windows用バッチファイル
├── ahiru.ps1               # PowerShell用スクリプト
├── main.py                 # AIのメインプログラム
├── vad_analyzer.py         # VADスコアを分析・算出するモジュール
├── duck_translator.py      # VADスコアに対応するアヒル語を選択するモジュール
│
├── data/
│   ├── duck_language.csv         # 基本のアヒル語表現データ
│   ├── duck_language_short.csv   # 短いアヒル語表現データ
│   ├── duck_language_long.csv    # 長いアヒル語表現データ
│   └── duck_language_neutral.csv # ニュートラルなアヒル語表現データ
│
└── README.md               # このファイル
```
