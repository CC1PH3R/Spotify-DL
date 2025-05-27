from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
from core import download_song
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎶 Welcome! Send me any song name and I’ll fetch it for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text(f"🔍 Searching for: {user_input}...")

    try:
        mp3_path = download_song(user_input)
        await update.message.reply_text("✅ Song is ready! Uploading now...")
        await update.message.reply_audio(audio=open(mp3_path, 'rb'))
    except Exception as e:
        await update.message.reply_text(f"❌ An error occurred: {str(e)}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Bot is unning...")
    app.run_polling()

if __name__ == "__main__":
    main()