# QUICK START GUIDE

## GitHubからZIPダウンロードした場合のセットアップ手順

### 1. ダウンロードと展開

1. **GitHubページからZIPをダウンロード**
   - `Code` → `Download ZIP` でダウンロード

2. **任意の場所に展開**

   ```txt
   例: C:\Users\[ユーザー名]\ahiru-code\
   例: D:\Projects\ahiru-code\
   ```

### 2. 必要なソフトウェアの確認

- **Python 3.8以上** が必要です
- 確認方法: コマンドプロンプトまたはPowerShellで `python --version`

### 3. セットアップ（自動）

展開したフォルダで以下のいずれかを実行：

**PowerShell（推奨）:**

```powershell
cd "展開したフォルダパス"
.\scripts\setup.ps1
```

**コマンドプロンプト:**

```cmd
cd "展開したフォルダパス"
scripts\setup.bat
```

### 4. ライブラリのインストール

```shell
pip install -r requirements.txt
```

### 5. 実行

セットアップ完了後、**新しいターミナルを開いて**以下のコマンドでどこからでも実行可能：

```shell
ahiru
```

---

## トラブルシューティング

### 「ahiruコマンドが見つからない」場合

1. **新しいターミナルを開く** （環境変数の反映のため）
2. **手動でPATH設定**：
   - `Win + R` → `sysdm.cpl` → 詳細設定 → 環境変数
   - ユーザー環境変数の「Path」に展開フォルダのパスを追加

### VS Codeで使用する場合

VS Codeのターミナルでは以下の方法：

#### 方法1: 直接実行

```powershell
.\ahiru.cmd
```

#### 方法2: PowerShell関数として登録

```powershell
.\scripts\vscode_setup.ps1
```

### PowerShell実行ポリシーエラーの場合

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## ファイルを移動した場合

フォルダを別の場所に移動した場合は、再度セットアップを実行してください：

```shell
.\scripts\setup.ps1
```

これでPATHが新しい場所に更新されます。
