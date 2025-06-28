#!/usr/bin/env python3
"""
AHIRU-CODE実行スクリプト
このスクリプトを実行することでアヒルAIを起動します。
"""

import sys
import os

# スクリプトのディレクトリをPythonパスに追加
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

# main.pyのmain関数を実行
if __name__ == "__main__":
    from main import main
    main()
