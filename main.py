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
  "21": "https://i.postimg.cc/m2GC0pzr/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-21.png",
  "22": "https://i.postimg.cc/05W5RbHc/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-22.png",
  "23": "https://i.postimg.cc/G373wHSQ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-23.png",
  "24": "https://i.postimg.cc/dQHQPLS6/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-24.png",
  "25": "https://i.postimg.cc/3rSr5db9/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-25.png",
  "26": "https://i.postimg.cc/658W9tkN/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-26.png",
  "27": "https://i.postimg.cc/ncXFHpyJ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-27.png",
  "28": "https://i.postimg.cc/ncXFHpyx/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-28.png",
  "29": "https://i.postimg.cc/kX2Jnq04/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-29.png",
  "30": "https://i.postimg.cc/X7tVqtWK/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-30.png",
  "31": "https://i.postimg.cc/Gh6ct6R8/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-31.png",
  "32": "https://i.postimg.cc/QxvXCvDW/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-32.png",
  "33": "https://i.postimg.cc/Wbx2zxV6/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-33.png",
  "34": "https://i.postimg.cc/Qd5jTSxs/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-34.png",
  "35": "https://i.postimg.cc/wjJ9mFT6/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-35.png",
  "36": "https://i.postimg.cc/3wTYCpdW/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-36.png",
  "37": "https://i.postimg.cc/YSHMfgh9/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-37.png",
  "38": "https://i.postimg.cc/6QfwH3vh/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-38.png",
  "39": "https://i.postimg.cc/fbfZHL98/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-39.png",
  "40": "https://i.postimg.cc/9fYVxM7v/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-40.png",
  "41": "https://i.postimg.cc/g0HdMJZ1/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-41.png",
  "42": "https://i.postimg.cc/Y9X7Hs8k/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-42.png",
  "43": "https://i.postimg.cc/MTZwgS0H/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-43.png",
  "44": "https://i.postimg.cc/JnT8L2Kn/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-44.png",
  "45": "https://i.postimg.cc/V67w8V4J/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-45.png",
  "46": "https://i.postimg.cc/rmhTkPgN/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-46.png",
  "47": "https://i.postimg.cc/SRJhNftc/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-47.png",
  "48": "https://i.postimg.cc/rsKkFNYW/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-48.png",
  "49": "https://i.postimg.cc/Fz74sVng/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-49.png",
  "50": "https://i.postimg.cc/zv61LH9c/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-50.png",
  "51": "https://i.postimg.cc/nrCJcGPZ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-51.png",
  "52": "https://i.postimg.cc/NFSwy2WZ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-52.png",
  "53": "https://i.postimg.cc/j2mrWnp0/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-53.png",
  "54": "https://i.postimg.cc/SR3pXYBK/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-54.png",
  "55": "https://i.postimg.cc/VvpcS0x6/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-55.png",
  "56": "https://i.postimg.cc/fyph3SGy/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-56.png",
  "57": "https://i.postimg.cc/HnRCJ8qV/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-57.png",
  "58": "https://i.postimg.cc/J728YSG2/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-58.png",
  "59": "https://i.postimg.cc/y6bKp2kp/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-59.png",
  "60": "https://i.postimg.cc/NGztCZ5d/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-60.png",
  "61": "https://i.postimg.cc/1RjS7bfd/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-61.png",
  "62": "https://i.postimg.cc/8k0GXx71/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-62.png",
  "63": "https://i.postimg.cc/VsVwZ2Jz/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-63.png",
  "64": "https://i.postimg.cc/v8Ny2C48/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-64.png",
  "65": "https://i.postimg.cc/T24xNBK3/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-65.png",
  "66": "https://i.postimg.cc/RVJBkGtZ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-66.png",
  "67": "https://i.postimg.cc/yY3HMnRY/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-67.png",
  "68": "https://i.postimg.cc/X7BbRx5p/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-68.png",
  "69": "https://i.postimg.cc/Fsk4MGSz/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-69.png",
  "70": "https://i.postimg.cc/fR4NDX73/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-70.png",
  "71": "https://i.postimg.cc/W1RvTrmF/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-71.png",
  "72": "https://i.postimg.cc/HWhJ0ZHj/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-72.png",
  "73": "https://i.postimg.cc/59RH571H/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-73.png",
  "74": "https://i.postimg.cc/zXHyxCXp/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-74.png",
  "75": "https://i.postimg.cc/CLnRcGLv/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-75.png",
  "76": "https://i.postimg.cc/nc9X34c5/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-76.png",
  "77": "https://i.postimg.cc/mgxtJPtd/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-77.png",
  "78": "https://i.postimg.cc/MpyvSzBm/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-78.png",
  "79": "https://i.postimg.cc/y8FkH7RF/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-79.png",
  "80": "https://i.postimg.cc/fbDkW179/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-80.png",
  "81": "https://i.postimg.cc/4xzmgXc5/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-81.png",
  "82": "https://i.postimg.cc/R0dhWGXh/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-82.png",
  "83": "https://i.postimg.cc/0NnjzZcQ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-83.png",
  "84": "https://i.postimg.cc/jjc2DvZW/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-84.png",
  "85": "https://i.postimg.cc/s2mxMKwM/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-85.png",
  "86": "https://i.postimg.cc/W343grHW/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-86.png",
  "87": "https://i.postimg.cc/d101rdx4/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-87.png",
  "88": "https://i.postimg.cc/cHJHwYbT/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-88.png",
  "89": "https://i.postimg.cc/d101rdx5/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-89.png",
  "90": "https://i.postimg.cc/mkv2vn2S/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-90.png",
  "91": "https://i.postimg.cc/Pf9xvCzC/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-91.png",
  "92": "https://i.postimg.cc/m29rYT8H/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-92.png",
  "93": "https://i.postimg.cc/65ZQrBYh/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-93.png",
  "94": "https://i.postimg.cc/kXS5Q7fZ/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-94.png",
  "95": "https://i.postimg.cc/vZdZXCKB/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-95.png",
  "96": "https://i.postimg.cc/8zBPYt8P/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-96.png",
  "97": "https://i.postimg.cc/3xCJqnM4/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-97.png",
  "98": "https://i.postimg.cc/mgN2n8x7/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-98.png",
  "99": "https://i.postimg.cc/Xvj76d31/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-99.png",
  "100": "https://i.postimg.cc/1tMFZsL0/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-100.png",
  "101": "https://i.postimg.cc/wBpRy1z1/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-101.png",
  "102": "https://i.postimg.cc/9fhwRD24/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-102.png",
  "103": "https://i.postimg.cc/W4vqFdVq/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-103.png",
  "104": "https://i.postimg.cc/fbftxMWC/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-104.png",
  "105": "https://i.postimg.cc/SKf2WmQT/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-105.png",
  "106": "https://i.postimg.cc/BvBLxJZV/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-106.png",
  "107": "https://i.postimg.cc/d0jk8JQX/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-107.png",
  "108": "https://i.postimg.cc/V6sSg2dk/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-108.png",
  "109": "https://i.postimg.cc/zBDL74Vf/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-109.png",
  "110": "https://i.postimg.cc/vB81hCcc/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-110.png",
  "111": "https://i.postimg.cc/DZfW6R8W/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-111.png",
  "112": "https://i.postimg.cc/63H8mzvb/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-112.png",
  "113": "https://i.postimg.cc/fLHVr59B/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-113.png",
  "114": "https://i.postimg.cc/26H1KTZK/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-114.png",
  "115": "https://i.postimg.cc/LXyJbv1G/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-115.png",
  "116": "https://i.postimg.cc/J0GsVJ3D/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-116.png",
  "117": "https://i.postimg.cc/J0vG1nKh/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-117.png",
  "118": "https://i.postimg.cc/fypJwL5R/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-118.png",
  "119": "https://i.postimg.cc/j2mLs5vs/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-119.png",
  "120": "https://i.postimg.cc/L4bqkCR9/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-120.png",
  "121": "https://i.postimg.cc/gcTwySdY/almkhtsr-fy-tfsyr-alqran-alkrym-altbʿt-alsadst-1-604-121.png"
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
