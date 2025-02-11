# commands.py
import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def send_message(chat_id, message, parse_mode="Markdown"):
    """发送消息到 Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": parse_mode  # 允许 Markdown 解析
    }
    response = requests.post(url, json=data)
    return response.json()

def start_command(update, context):
    """处理 /start 命令"""
    user = update.effective_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name

    message = f"Hello, {first_name} {last_name}!\n"
    # 在这里添加检查用户是否已记录的信息的逻辑
    # 例如，从数据库或文件中查询
    user_info_recorded = False  # 假设用户未记录信息

    if not user_info_recorded:
        message += "Welcome to this bot!\n"
        message += "Please use /my <account> <password> to record your information."
    else:
        message += "Welcome back!"

    send_message(update.effective_chat.id, message)

def my_command(update, context):
    """处理 /my 命令，记录用户信息"""
    args = context.args
    if len(args) == 2:
        account = args[0]
        password = args[1]
        # 在这里添加记录用户信息的逻辑
        # 例如，将用户信息存储到数据库或文件中
        message = f"Your account: {account} and password: {password} have been recorded."
    else:
        message = "Usage: /my <account> <password>"

    send_message(update.effective_chat.id, message)

def email_command(update, context):
    """处理 /email 命令，绑定用户邮箱"""
    args = context.args
    if len(args) == 1:
        email = args[0]
        # 在这里添加绑定用户邮箱的逻辑
        # 例如，将邮箱信息存储到数据库中
        message = f"Your email: {email} has been bound."
    else:
        message = "Usage: /email <email>"

    send_message(update.effective_chat.id, message)

def about_command(update, context):
    """处理 /about 命令，获取作者信息"""
    message = "This bot is created by Johnson Maliya (@Lw0304)."
    send_message(update.effective_chat.id, message)

def goods_command(update, context):
    """处理 /goods 命令，获取推荐信息"""
    # 这里可以自定义推荐信息
    message = "Here are some recommended items:\n"
    message += "- Item 1\n"
    message += "- Item 2\n"
    message += "- Item 3"
    send_message(update.effective_chat.id, message)
