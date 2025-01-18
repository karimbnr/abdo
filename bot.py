import os
from telegram.ext import Updater, CommandHandler

# جلب TOKEN من المتغير البيئي
TOKEN = os.getenv("7725005982:AAFdU4hhpQduvWOTnsN5e5--dDbC7lBtlmo")

def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت تيليجرام الخاص بك.")

def main():
    if not TOKEN:
        print("Error: TOKEN not found!")
        return

    # إعداد البوت
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # ربط أمر /start بالدالة start
    dispatcher.add_handler(CommandHandler("start", start))

    # تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
