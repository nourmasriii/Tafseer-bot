import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler, filters

# خذ رقم البورت من متغيرات البيئة (Render)
PORT = int(os.environ.get("PORT", 10000))


# صفحة التفسير المختصر 1 فقط
short_tafsir_pages = {
    "1": "https://i.postimg.cc/SRbqR4Zj/IMG-20250707-202815-062.jpg"
}


BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8443))


# دالة التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # فقط إذا الرسالة بصيغة صحيحة
    if text == "التفسير المختصر صفحة 1":
        await update.message.reply_photo(short_tafsir_pages["1"])
    # غير هيك → ما يرد نهائيًا

async def send_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    page = update.message.text.strip()

    if page.isdigit() and page in pages:
        await update.message.reply_photo(photo=pages[page])
    # غير هيك، يسكت تماماً وما يرد بشيء
    
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_page))

    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}"

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=webhook_url,
    )
    print(f"✅ Webhook set to {webhook_url}")

if name == "main":
    main()
