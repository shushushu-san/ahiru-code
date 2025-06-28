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

### 🚀 クイックスタート（GitHubからダウンロードした場合）

**前提条件:** Python 3.8以上がインストールされていること

1. **ライブラリをインストール**

   ```shell
   pip install -r requirements.txt
   ```

2. **自動セットアップを実行** （どこからでもahiruコマンドを使えるようにする）

   **PowerShell（推奨）:**

   ```powershell
   .\scripts\setup.ps1
   ```

   **コマンドプロンプト:**

   ```cmd
   scripts\setup.bat
   ```

3. **新しいターミナルを開いて実行**

   ```shell
   ahiru
   ```

### 📋 詳細なセットアップ手順

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
   scripts\setup.bat
   ```

   **PowerShell実行ポリシーエラーが出る場合:**

   ```shell
   .\scripts\setup.ps1
   ```

   **PATH設定確認:**

   ```shell
   .\scripts\check_path.bat
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
   # どこからでも実行可能（PATH設定後）
   ahiru
   ```

   **方法2: Pythonスクリプトとして直接実行**

   ```shell
   python scripts\ahiru.py
   ```

   **方法3: メインファイルを直接実行**

   ```shell
   python main.py
   ```

4. コンソールに日本語で話しかけると、アヒルAIがアヒル語で応答します。終了するには `exit` または`さようなら`と入力してください。

### 🖥️ VS Code環境での使用

VS CodeのPowerShellターミナルで使用する場合：

#### 方法1: PowerShell関数として登録（推奨）

```powershell
.\scripts\vscode_setup.ps1
```

VS Code再起動後、どこからでも `ahiru` コマンドが使用可能

#### 方法2: 直接実行

```powershell
.\ahiru.cmd
# または
python scripts\ahiru.py
```

## ファイル構造

```text
ahiru-code/
│
├── README.md               # このファイル
├── QUICK_START.md          # GitHubダウンロード用クイックスタートガイド
├── requirements.txt        # 必要なライブラリ一覧
├── ahiru.cmd               # メイン実行ファイル（ユーザー用）
│
├── src/                    # ソースコード
│   ├── main.py             # AIのメインプログラム
│   ├── vad_analyzer.py     # VADスコアを分析・算出するモジュール
│   └── duck_translator.py  # VADスコアに対応するアヒル語を選択するモジュール
│
├── scripts/                # 実行・セットアップスクリプト
│   ├── ahiru.py            # Python実行スクリプト
│   ├── ahiru_ps.ps1        # PowerShell用スクリプト
│   ├── ahiru_profile.ps1   # PowerShell関数定義
│   ├── vscode_setup.ps1    # VS Code用セットアップスクリプト
│   ├── setup.bat           # セットアップスクリプト（CMD用）
│   ├── setup.ps1           # セットアップスクリプト（PowerShell用）
│   └── check_path.bat      # PATH設定確認スクリプト
│
├── tools/                  # 開発・デバッグツール
│   ├── test_ahiru.ps1      # ahiruコマンドテストスクリプト
│   ├── debug_pathext.bat   # PATHEXT確認スクリプト
│   └── cleanup.bat         # ファイルクリーンアップスクリプト
│
├── data/                   # データファイル
│   ├── duck_language.csv         # 基本のアヒル語表現データ
│   ├── duck_language_short.csv   # 短いアヒル語表現データ
│   ├── duck_language_long.csv    # 長いアヒル語表現データ
│   └── duck_language_neutral.csv # ニュートラルなアヒル語表現データ
│
└── assets/                 # アセット
    └── ascii_art.txt       # ASCIIアート
```
