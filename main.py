import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = os.environ.get("USER_ID") # 从环境变量中读取
    if not user_id:
        await update.message.reply_text("未配置 USER_ID 环境变量")
        return
    await update.message.reply_text(f"欢迎使用机器人，USER_ID: {user_id}!")

def main() -> None:
    bot_token = os.environ.get("BOT_TOKEN") # 从环境变量中读取

    if not bot_token:
        print("错误：未设置 BOT_TOKEN 环境变量。")
        return

    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
