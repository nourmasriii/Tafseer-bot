import os
import asyncio
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
        "أرسل: 201 لتحصل على صفحة التفسير المقابلة."
    )

# إرسال الصفحة
async def send_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    page = update.message.text.strip()
    if page in tafsir_pages_new:
        await update.message.reply_photo(photo=tafsir_pages_new[page])

# نبضة الحياة
async def send_heartbeat(app):
    while True:
        try:
            await app.bot.send_message(chat_id=OWNER_CHAT_ID,
                                       text="📘 بوت صفحات القرآن شغال - نبضة حياة")
            print("✅ نبضة حياة أُرسلت")
        except Exception as e:
            print("❌ خطأ في إرسال نبضة الحياة:", e)
        await asyncio.sleep(600)  # كل 10 دقائق

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_page))

    # تشغيل نبضة الحياة كـ task بعد build
    asyncio.create_task(send_heartbeat(app))

    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}"
    print(f"✅ Webhook set to {webhook_url}")

    # تشغيل التطبيق (run_webhook يدير event loop بنفسه)
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=webhook_url,
    )

if __name__ == "__main__":
    main()
