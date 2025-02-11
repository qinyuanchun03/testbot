import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def send_message(chat_id, message):
    """发送消息到 Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"  # 使用 Markdown 解析文本
    }
    response = requests.post(url, json=data)
    return response.json()

def start_command(chat_id, user_id, first_name, last_name):
    """处理 /start 命令"""
    message = f"Hello, {first_name} {last_name}!\n"
    # 这里可以添加检查用户是否已记录的信息，如果未记录，提示用户使用 /my 命令
    message += "Welcome to this bot!\n"
    message += "Please use /my <account> <password> to record your information."
    send_message(chat_id, message)

def my_command(chat_id, account, password):
    """处理 /my 命令，记录用户信息"""
    # 这里需要实现记录用户信息的逻辑，例如存储到数据库或文件中
    # 这里只是一个示例，简单地回复用户
    message = f"Your account: {account} and password: {password} have been recorded."
    send_message(chat_id, message)

def email_command(chat_id, email):
    """处理 /email 命令，绑定用户邮箱"""
    # 这里需要实现绑定用户邮箱的逻辑
    # 这里只是一个示例，简单地回复用户
    message = f"Your email: {email} has been bound."
    send_message(chat_id, message)

def about_command(chat_id):
    """处理 /about 命令，获取作者信息"""
    message = "This bot is created by Johnson Maliya (@Lw0304)."
    send_message(chat_id, message)

def goods_command(chat_id):
    """处理 /goods 命令，获取推荐信息"""
    # 这里可以自定义推荐信息
    message = "Here are some recommended items:\n"
    message += "- Item 1\n"
    message += "- Item 2\n"
    message += "- Item 3"
    send_message(chat_id, message)

# 在这里添加其他命令处理函数

def handle_command(update):
    """处理用户发送的消息"""
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text")
    if not text:
        return
    
    user = message.get("from")
    user_id = user.get("id")
    first_name = user.get("first_name")
    last_name = user.get("last_name")

    if text.startswith("/start"):
        start_command(chat_id, user_id, first_name, last_name)
    elif text.startswith("/my"):
        parts = text.split()
        if len(parts) == 3:
            account = parts[1]
            password = parts[2]
            my_command(chat_id, account, password)
        else:
            send_message(chat_id, "Usage: /my <account> <password>")
    elif text.startswith("/email"):
        parts = text.split()
        if len(parts) == 2:
            email = parts[1]
            email_command(chat_id, email)
        else:
            send_message(chat_id, "Usage: /email <email>")
    elif text.startswith("/about"):
        about_command(chat_id)
    elif text.startswith("/goods"):
        goods_command(chat_id)
    # 在这里添加其他命令处理逻辑
    else:
        send_message(chat_id, "I don't understand this command.")
