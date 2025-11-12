import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# ⚡ هنا تضعي كل الصفحات من 1 إلى 604
# مثال:
tafsir_pages = {
  "1": "https://i.postimg.cc/L81Dzg1J/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-1.png",
  "2": "https://i.postimg.cc/J0jJsZgt/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-2.png",
  "3": "https://i.postimg.cc/VkfMNSFQ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-3.png",
  "4": "https://i.postimg.cc/k5DbxkZx/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-4.png",
  "5": "https://i.postimg.cc/bvdtQKMK/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-5.png",
  "6": "https://i.postimg.cc/1RDNc0CX/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-6.png",
  "7": "https://i.postimg.cc/8kLrBdKk/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-7.png",
  "8": "https://i.postimg.cc/QNcWkg43/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-8.png",
  "9": "https://i.postimg.cc/3J70LyVC/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-9.png",
  "10": "https://i.postimg.cc/wThcMY81/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-10.png",
  "11": "https://i.postimg.cc/GmdPsgdJ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-11.png",
  "12": "https://i.postimg.cc/7YgMhr8b/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-12.png",
  "13": "https://i.postimg.cc/Ls0jwHfV/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-13.png",
  "14": "https://i.postimg.cc/cJJQFKK2/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-14.png",
  "15": "https://i.postimg.cc/mr67JbMw/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-15.png",
  "16": "https://i.postimg.cc/q7Z2SknW/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-16.png",
  "17": "https://i.postimg.cc/C1BbVWsh/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-17.png",
  "18": "https://i.postimg.cc/fLtYh6ff/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-18.png",
  "19": "https://i.postimg.cc/k40KMfTL/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-19.png",
  "20": "https://i.postimg.cc/dtKrzNkM/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-20.png",
  "21": "https://i.postimg.cc/m2GC0pzr/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-21.png"
}

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8443))
OWNER_CHAT_ID = 6115157843  # ضع هنا رقمك الشخصي

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 مرحباً بك في بوت التفسير المختصر.\n"
        "أرسل: المختصر 1 إلى 604 لتحصل على صفحة التفسير المقابلة."
    )

# إرسال الصفحة
async def send_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text.strip()
    
    # التأكد أن الرسالة تبدأ بـ "المختصر"
    if text.startswith("المختصر"):
        page = text.replace("المختصر", "").strip()
        if page in tafsir_pages:
            await update.message.reply_photo(photo=tafsir_pages[page])
        else:
            await update.message.reply_text("❌ هذه الصفحة غير موجودة حالياً.")

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
