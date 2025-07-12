import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# روابط صفحات التفسير من 1 إلى 50
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
    "25": "https://i.postimg.cc/8zfjPDXN/0025.jpg",
    "26": "https://i.postimg.cc/nc3fcWNc/0026.jpg",
    "27": "https://i.postimg.cc/Dzb96w08/0027.jpg",
    "28": "https://i.postimg.cc/t4f0FxXK/0028.jpg",
    "29": "https://i.postimg.cc/t47Q15Hd/0029.jpg",
    "30": "https://i.postimg.cc/gJFfTbL4/0030.jpg",
    "31": "https://i.postimg.cc/vBrpR2Wy/0031.jpg",
    "32": "https://i.postimg.cc/90cscPp7/0032.jpg",
    "33": "https://i.postimg.cc/Znj2n97D/0033.jpg",
    "34": "https://i.postimg.cc/pVBgq7WY/0034.jpg",
    "35": "https://i.postimg.cc/VLL2TR5y/0035.jpg",
    "36": "https://i.postimg.cc/FsWwQLJY/0036.jpg",
    "37": "https://i.postimg.cc/y8Dt68Fv/0037.jpg",
    "38": "https://i.postimg.cc/g215xbsd/0038.jpg",
    "39": "https://i.postimg.cc/wvpGk5nG/0039.jpg",
    "40": "https://i.postimg.cc/FRVnCd4s/0040.jpg",
    "41": "https://i.postimg.cc/7hPtFHH1/0041.jpg",
    "42": "https://i.postimg.cc/L5yQRc5c/0042.jpg",
    "43": "https://i.postimg.cc/bYLBQtgm/0043.jpg",
    "44": "https://i.postimg.cc/qMRZQvZ4/0044.jpg",
    "45": "https://i.postimg.cc/J42YFC9J/0045.jpg",
    "46": "https://i.postimg.cc/L8gQK0pW/0046.jpg",
    "47": "https://i.postimg.cc/43CLJb4x/0047.jpg",
    "48": "https://i.postimg.cc/wBhW3y3c/0048.jpg",
    "49": "https://i.postimg.cc/JnMpXrkw/0049.jpg",
    "50": "https://i.postimg.cc/W38X6BGd/0050.jpg"
}

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

OWNER_CHAT_ID = 6115157843  # رقم صاحب البوت

# دالة إرسال صورة التفسير عند استقبال "المختصر رقم"
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
        except:
            pass

# دالة نبضة الحياة
async def send_heartbeat(bot):
    try:
        await bot.send_message(chat_id=OWNER_CHAT_ID, text="🔔 البوت شغال - نبضة حياة")
    except Exception as e:
        print(f"❌ خطأ في إرسال نبضة الحياة: {e}")

# تشغيل الجدولة عند بدء البوت
async def on_startup(app):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_heartbeat, 'interval', minutes=10, args=[app.bot])
    scheduler.start()
    print("✅ Scheduler started")

def main():
    app =
    ApplicationBuilder().token(BOT_TOKEN).post_init(on_startup).build()
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
