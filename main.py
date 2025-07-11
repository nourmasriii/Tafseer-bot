import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# التفسير (رابط صورة أو نص حسب ما تريدي)
tafsir_pages = {
    {
  "0001": "https://i.postimg.cc/5ttKF7v4/0001.jpg",
  "0002": "https://i.postimg.cc/4xsSXNxh/0002.jpg",
  "0003": "https://i.postimg.cc/mgj6kfPp/0003.jpg",
  "0004": "https://i.postimg.cc/hG3y8Lb9/0004.jpg",
  "0005": "https://i.postimg.cc/tTZrBs28/0005.jpg",
  "0006": "https://i.postimg.cc/XJRsmnPq/0006.jpg",
  "0007": "https://i.postimg.cc/nhF06R34/0007.jpg",
  "0008": "https://i.postimg.cc/fbk5b3nk/0008.jpg",
  "0009": "https://i.postimg.cc/FRLZj2K4/0009.jpg",
  "0010": "https://i.postimg.cc/c1fh6yj7/0010.jpg",
  "0011": "https://i.postimg.cc/g2tq1YXp/0011.jpg",
  "0012": "https://i.postimg.cc/brR1g8cK/0012.jpg",
  "0013": "https://i.postimg.cc/vH3W6Qvn/0013.jpg",
  "0014": "https://i.postimg.cc/8CrW3Lgd/0014.jpg",
  "0015": "https://i.postimg.cc/KjQgLNtb/0015.jpg",
  "0016": "https://i.postimg.cc/T3KWLn18/0016.jpg",
  "0017": "https://i.postimg.cc/q7nhQ02j/0017.jpg",
  "0018": "https://i.postimg.cc/3RTyc6B7/0018.jpg",
  "0019": "https://i.postimg.cc/267qRwcW/0019.jpg",
  "0020": "https://i.postimg.cc/QCNFXTwy/0020.jpg",
  "0021": "https://i.postimg.cc/vTPcDmdH/0021.jpg",
  "0022": "https://i.postimg.cc/T2QyttWM/0022.jpg",
  "0023": "https://i.postimg.cc/8P579LhF/0023.jpg",
  "0024": "https://i.postimg.cc/Gh54C9QX/0024.jpg",
  "0025": "https://i.postimg.cc/8zfjPDXN/0025.jpg"
    }

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

# التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if text.startswith("تفسير صفحة"):
        try:
            page_num = int(text.replace("تفسير صفحة", "").strip())
            page_key = f"{page_num:04}"  # مثل 0001، 0002 ...
            if page_key in tafsir_pages:
                await update.message.reply_photo(photo=tafsir_pages[page_key])

# تشغيل البوت بـ Webhook
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
