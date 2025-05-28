#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """執行 Django 管理指令的主函式"""
    # 設定 Django 專案的設定檔路徑
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comment_project.settings")
    try:
        # 匯入 Django 的指令列執行工具
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 若未安裝 Django，顯示錯誤訊息
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 執行指令列傳入的 Django 指令
    execute_from_command_line(sys.argv)

# 當此檔案被直接執行時，呼叫 main() 函式
if __name__ == "__main__":
    main()