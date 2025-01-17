from telegram import Bot
from telegram.ext import Updater, CommandHandler

# استبدل هذا بالقيمة الخاصة بك من BotFather على تيليجرام
TOKEN = '7725005982:AAFdU4hhpQduvWOTnsN5e5--dDbC7lBtlmo'

def start(update, context):
    update.message.reply_text('مرحبًا! أنا بوت تيليجرام الخاص بك.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # إضافة وظيفة /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
