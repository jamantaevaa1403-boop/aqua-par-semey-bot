from flask import Flask
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater

import os

TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route('/')
def home():
    return "Aqua Par Semey Telegram Bot is running!"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Добро пожаловать в Aqua Par Semey! 💧")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
