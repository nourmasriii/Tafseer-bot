import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

API_TOKEN = os.environ.get("BOT_TOKEN")

short_tafsir_pages = {
    "1": "https://i.postimg.cc/SRbqR4Zj/IMG-20250707-202815-062.jpg"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith("التفسير المختصر صفحة"):
        try:
            page_num = text.split("صفحة")[1].strip()
            if page_num in short_tafsir_pages:
                await update.message.reply_photo(short_tafsir_pages[page_num])
        except:
            pass

if __name__ == "__main__":
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
