from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# توكن البوت
BOT_TOKEN = "7738093918:AAFM1h73-v2tD5lnXQQ8RbvDKpOPYGhy_JM"

# صفحة التفسير المختصر 1 فقط
short_tafsir_pages = {
    "1": "https://i.postimg.cc/SRbqR4Zj/IMG-20250707-202815-062.jpg"
}

# دالة التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # فقط إذا الرسالة بصيغة صحيحة
    if text == "التفسير المختصر صفحة 1":
        await update.message.reply_photo(short_tafsir_pages["1"])
    # غير هيك → ما يرد نهائيًا

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ البوت شغّال...")
    app.run_polling()

if __name__ == "__main__":
    main()
