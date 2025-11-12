import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# صفحة واحدة للتجربة
tafsir_pages_new = {
    "201": "https://i.postimg.cc/ry44Pw3n/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-201.png"
}

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8443))
OWNER_CHAT_ID = 6115157843  # ضع هنا رقمك الشخصي

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 مرحباً بك في بوت التفسير المختصر.\n"
        "أرسل: المختصر 201 لتحصل على صفحة التفسير."
    )

# إرسال الصفحة
async def send_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text.strip()
    
    # التأكد أن الرسالة تبدأ بـ "المختصر" ثم الرقم
    if text.startswith("المختصر"):
        page = text.replace("المختصر", "").strip()
        if page in tafsir_pages_new:
            await update.message.reply_photo(photo=tafsir_pages_new[page])

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # إضافة handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_page))

    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}"
    print(f"✅ Webhook set to {webhook_url}")

    # تشغيل التطبيق (run_webhook يدير الـ event loop)
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=webhook_url,
    )

if __name__ == "__main__":
    main()
