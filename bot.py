import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Aqua Par Semey bot работает через Flask!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Бот Aqua Par Semey запущен и готов!")

def run_bot():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ Ошибка: переменная BOT_TOKEN не найдена")
        return
    app_tg = ApplicationBuilder().token(token).build()
    app_tg.add_handler(CommandHandler("start", start))
    print("🚀 Telegram бот запущен")
    app_tg.run_polling()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    print(f"🌐 Flask сервер запущен на порту {port}")
    app.run(host="0.0.0.0", port=port)
