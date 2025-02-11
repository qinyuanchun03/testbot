# commands.py
import os
import requests
import logging

logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def send_message(chat_id, message, parse_mode="Markdown"):
    """发送消息到 Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": parse_mode  # 允许 Markdown 解析
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # 检查响应状态码
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending message: {e}")
        return None

async def start_command(update, context):
    """处理 /start 命令"""
    # ... (其他代码)

async def my_command(update, context):
    """处理 /my 命令"""
    # ... (其他代码)

async def email_command(update, context):
    """处理 /email 命令"""
    # ... (其他代码)

async def about_command(update, context):
    """处理 /about 命令"""
    # ... (其他代码)

async def goods_command(update, context):
    """处理 /goods 命令"""
    # ... (其他代码)
