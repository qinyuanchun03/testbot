# main.py
import os
import logging
from dotenv import load_dotenv
from telegram import Application
from commands import start_command, my_command, email_command, about_command, goods_command

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
