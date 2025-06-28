#!/usr/bin/env python3
"""
AHIRU-CODE実行スクリプト
このスクリプトを実行することでアヒルAIを起動します。
"""

import sys
import os

# スクリプトの親ディレクトリ（プロジェクトルート）をPythonパスに追加
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)  # 親ディレクトリ（プロジェクトルート）
sys.path.insert(0, project_root)

# main.pyのmain関数を実行（srcフォルダから）
if __name__ == "__main__":
    # srcフォルダもパスに追加
    src_dir = os.path.join(project_root, 'src')
    sys.path.insert(0, src_dir)
    from main import main
    main()
