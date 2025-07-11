import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# روابط صفحات التفسير من 1 إلى 25
tafsir_pages = {
    "1": "https://i.postimg.cc/5ttKF7v4/0001.jpg",
    "2": "https://i.postimg.cc/4xsSXNxh/0002.jpg",
    "3": "https://i.postimg.cc/mgj6kfPp/0003.jpg",
    "4": "https://i.postimg.cc/hG3y8Lb9/0004.jpg",
    "5": "https://i.postimg.cc/tTZrBs28/0005.jpg",
    "6": "https://i.postimg.cc/XJRsmnPq/0006.jpg",
    "7": "https://i.postimg.cc/nhF06R34/0007.jpg",
    "8": "https://i.postimg.cc/fbk5b3nk/0008.jpg",
    "9": "https://i.postimg.cc/FRLZj2K4/0009.jpg",
    "10": "https://i.postimg.cc/c1fh6yj7/0010.jpg",
    "11": "https://i.postimg.cc/g2tq1YXp/0011.jpg",
    "12": "https://i.postimg.cc/brR1g8cK/0012.jpg",
    "13": "https://i.postimg.cc/vH3W6Qvn/0013.jpg",
    "14": "https://i.postimg.cc/8CrW3Lgd/0014.jpg",
    "15": "https://i.postimg.cc/KjQgLNtb/0015.jpg",
    "16": "https://i.postimg.cc/T3KWLn18/0016.jpg",
    "17": "https://i.postimg.cc/q7nhQ02j/0017.jpg",
    "18": "https://i.postimg.cc/3RTyc6B7/0018.jpg",
    "19": "https://i.postimg.cc/267qRwcW/0019.jpg",
    "20": "https://i.postimg.cc/QCNFXTwy/0020.jpg",
    "21": "https://i.postimg.cc/vTPcDmdH/0021.jpg",
    "22": "https://i.postimg.cc/T2QyttWM/0022.jpg",
    "23": "https://i.postimg.cc/8P579LhF/0023.jpg",
    "24": "https://i.postimg.cc/Gh54C9QX/0024.jpg",
    "25": "https://i.postimg.cc/8zfjPDXN/0025.jpg"
}

# قراءة التوكن والمنفذ من المتغيرات البيئية
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

# التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text.startswith("تفسير صفحة"):
        try:
            page_num = int(text.replace("تفسير صفحة", "").strip())
            page_key = str(page_num)
            if page_key in tafsir_pages:
                await update.message.reply_photo(photo=tafsir_pages[page_key])
        except:
            pass  # تجاهل أي أخطاء بصمت

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
