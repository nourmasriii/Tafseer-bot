import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# صفحة واحدة للتجربة
tafsir_pages_new = {
    "201": "https://i.postimg.cc/ry44Pw3n/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-201.png"
}

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))
OWNER_CHAT_ID = 6115157843

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 مرحباً بك في بوت التفسير المختصر.\n"
        "أرسل: المختصر 201 لتحصل على صفحة التفسير المقابلة."
    )

# رسائل التفسير
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text.strip()
    if text.startswith("المختصر"):
        try:
            page_num = int(text.replace("المختصر", "").strip())
            page_key = str(page_num)
            if page_key in tafsir_pages:
                await update.message.reply_photo(photo=tafsir_pages[page_key])
            else:
                await update.message.reply_text("❌ الصفحة غير موجودة حالياً.")
        except Exception as e:
            print("⚠️ خطأ:", e)

# نبضات الحياة
async def send_heartbeat(application):
    while True:
        try:
            await application.bot.send_message(chat_id=OWNER_CHAT_ID,
                                               text="📘 بوت التفسير المختصر شغال - نبضة حياة")
            print("✅ نبضة حياة أُرسلت")
        except Exception as e:
            print("❌ فشل إرسال النبضة:", e)
        await asyncio.sleep(600)  # كل 10 دقائق

# التشغيل
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # إضافة handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}"
    print(f"✅ Webhook: {webhook_url}")

    # تشغيل الـ heartbeat بعد بدء التطبيق
    async def runner():
        asyncio.create_task(send_heartbeat(app))
        await app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=webhook_url,
        )

    asyncio.run(runner())

if __name__ == "__main__":
    main()
