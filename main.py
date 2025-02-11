import os
import logging
from dotenv import load_dotenv
from telegram import Application
from telegram.ext import CommandHandler
import requests

load_dotenv()

# 配置日志记录
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
# ... (其他环境变量)

async def error_handler(update, context):
    """处理 Telegram API 错误"""
    logger.error(f"Update {update} caused error {context.error}")

async def post_init(application: Application):
    """机器人启动后执行的操作"""
    logger.info("Bot started.")

# --- 命令处理函数 ---
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

    await send_message(update.effective_chat.id, message)

async def my_command(update, context):
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

    await send_message(update.effective_chat.id, message)

async def email_command(update, context):
    """处理 /email 命令，绑定用户邮箱"""
    args = context.args
    if len(args) == 1:
        email = args[0]
        # 在这里添加绑定用户邮箱的逻辑
        # 例如，将邮箱信息存储到数据库中
        message = f"Your email: {email} has been bound."
    else:
        message = "Usage: /email <email>"

    await send_message(update.effective_chat.id, message)

async def about_command(update, context):
    """处理 /about 命令，获取作者信息"""
    message = "This bot is created by Johnson Maliya (@Lw0304)."
    await send_message(update.effective_chat.id, message)

async def goods_command(update, context):
    """处理 /goods 命令，获取推荐信息"""
    # 这里可以自定义推荐信息
    message = "Here are some recommended items:\n"
    message += "- Item 1\n"
    message += "- Item 2\n"
    message += "- Item 3"
    await send_message(update.effective_chat.id, message)
# --- 命令处理函数结束 ---

async def main():
    """启动机器人"""
    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    # 添加命令处理函数
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("my", my_command))
    application.add_handler(CommandHandler("email", email_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("goods", goods_command))

    # 添加错误处理函数
    application.add_error_handler(error_handler)

    await application.initialize()
    await application.start_polling()
    await application.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
