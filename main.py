import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# رابط الصفحة الوحيدة للتفسير المختصر
short_tafsir_pages = {
    "1": "https://i.postimg.cc/SRbqR4Zj/IMG-20250707-202815-062.jpg"
}

# جلب التوكن والبورت من متغيرات البيئة (Render)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

# الدالة التي تتعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "التفسير المختصر صفحة 1":
        await update.message.reply_photo(short_tafsir_pages["1"])
    # غير هيك، لا ترد بشيء

# تشغيل البوت باستخدام Webhook
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}"

    print(f"✅ Webhook set to {webhook_url}")

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=webhook_url,
    )

if __name__ == "__main__":
    main()
