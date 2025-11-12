import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# روابط صفحات التفسير من 1 إلى 50
tafsir_pages = {
  "1": "https://i.postimg.cc/50vgxqKt/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-1.png"
}
    
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))
OWNER_CHAT_ID = 6115157843

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 مرحباً بك في بوت التفسير المختصر.\n"
        "أرسل: المختصر 12 (أو أي رقم من 1 إلى 50) لتحصل على صورة التفسير المقابلة."
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
        except Exception as e:
            print("⚠️ خطأ:", e)

# نبضات الحياة
async def send_heartbeat(context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_message(chat_id=OWNER_CHAT_ID, text="📘 بوت التفسير المختصر شغال - نبضة حياة")
        print("✅ نبضة حياة أُرسلت")
    except Exception as e:
        print("❌ فشل إرسال النبضة:", e)

# بعد بدء التشغيل
async def on_startup(application):
    application.job_queue.run_repeating(send_heartbeat, interval=600, first=10)
    print("✅ JobQueue تم تشغيله")

# التشغيل
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(on_startup).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}"
    print(f"✅ Webhook: {webhook_url}")

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=webhook_url,
    )

if __name__ == "__main__":
    main()
