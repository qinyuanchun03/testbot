import logging
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, PicklePersistence

# 定义 Bot Token 和 API 地址
BOT_TOKEN = "YOUR_BOT_TOKEN"  # 替换为你的 Bot Token
API_URL = "https://api.telegram.org/bot"  # 默认 Telegram Bot API 地址 (通常不需要修改)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message and stores the chat ID."""
    chat_id = update.effective_chat.id
    context.user_data['chat_id'] = chat_id  # Store chat ID in user_data
    await context.bot.send_message(
        chat_id=chat_id,
        text="欢迎使用机器人！"
    )

async def send_data(context: ContextTypes.DEFAULT_TYPE):
    """Sends data to all users who have started the bot."""
    data = "这是一条广播消息！"  # 替换为你要发送的数据

    # Iterate over all user data and send the message
    for user_id, user_data in context.application.user_data.items():
        if 'chat_id' in user_data:
            chat_id = user_data['chat_id']
            try:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=data
                )
                logging.info(f"Data sent to user ID: {user_id}, chat ID: {chat_id}")
            except telegram.error.TelegramError as e:
                logging.error(f"Failed to send data to user ID: {user_id}, chat ID: {chat_id}: {e}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even when
    # the message is no longer available.
    logging.error(msg="Exception raised while handling an update:", exc_info=context.error)

    # Optionally, send the error to the user.
    await update.message.reply_text(f"An error occurred: {context.error}")


if __name__ == '__main__':
    # Enable persistence to store user data
    persistence = PicklePersistence(filepath="bot_data.pkl")

    # 使用 BOT_TOKEN 和 API_URL
    application = ApplicationBuilder().token(BOT_TOKEN).base_url(API_URL).persistence(persistence).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))

    # Run send_data every 60 seconds
    application.job_queue.run_repeating(send_data, interval=60, first=10)

    # Add error handler
    application.add_error_handler(error_handler)

    application.run_polling()
