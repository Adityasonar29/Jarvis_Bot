from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = ""  # Replace with your bot token from BotFather

# Command: /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am your bot.")

# Command: /help
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("You can use /start to interact with me.")

# Echo all text messages
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"You said: {update.message.text}")

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
