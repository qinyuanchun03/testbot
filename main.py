import os
import requests
import datetime
from dotenv import load_dotenv  # 导入 load_dotenv

load_dotenv()  # 加载 .env 文件 (本地测试用)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set.")

USER_ID = os.environ.get("USER_ID")
if not USER_ID:
    raise ValueError("USER_ID environment variable not set.")

FIRST_NAME = os.environ.get("FIRST_NAME")
if not FIRST_NAME:
    raise ValueError("FIRST_NAME environment variable not set.")

LAST_NAME = os.environ.get("LAST_NAME")
if not LAST_NAME:
    raise ValueError("LAST_NAME environment variable not set.")

LANG = os.environ.get("LANG")
if not LANG:
    raise ValueError("LANG environment variable not set.")


# ... (其他代码不变)

def main():
    # ... (其他代码不变)
    while True:
        update = {
            "message": {
                "chat": {"id": USER_ID},
                "from": {"id": USER_ID, "first_name": FIRST_NAME, "last_name": LAST_NAME},
                "text": input("Enter message: ")  # 从命令行输入消息
            }
        }
        handle_command(update)


if __name__ == "__main__":
    main()
