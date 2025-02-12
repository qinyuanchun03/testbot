import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import config  # 导入 config.py
from handlers import start, submenu

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even when
    # the message is no longer available.
    logging.error(msg="Exception raised while handling an update:", exc_info=context.error)

    # Optionally, send the error to the user.
    await update.message.reply_text(f"An error occurred: {context.error}")


if __name__ == '__main__':
    application = ApplicationBuilder().token(config.BOT_TOKEN).build()  # 使用 config.BOT_TOKEN

    # Register handlers
    application.add_handler(CommandHandler("start", start.start))
    application.add_handler(CommandHandler("option1", submenu.option1))  # 示例子菜单命令
    application.add_handler(CommandHandler("option2", submenu.option2))  # 示例子菜单命令

    # Add error handler
    application.add_error_handler(error_handler)

    application.run_polling()
