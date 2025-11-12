import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler

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
async def send_heartbeat(bot):
    try:
        await bot.send_message(chat_id=OWNER_CHAT_ID,
                               text="📘 بوت صفحات القرآن شغال - نبضة حياة")
    except Exception as e:
        print(f"⚠️ خطأ في إرسال نبضة الحياة: {e}")

# تشغيل الجدولة
def setup_scheduler(app):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_heartbeat, 'interval', minutes=10, args=[app.bot])
    scheduler.start()
    print("✅ Scheduler started")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_page))

    # جدولة نبضة الحياة
    setup_scheduler(app)

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
