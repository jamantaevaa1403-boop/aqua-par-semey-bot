import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- Flask для проверки Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Тест Flask работает на Render!"

# --- Простой Telegram бот ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Тестовый бот Aqua Par Semey работает!")

def run_telegram():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ Нет BOT_TOKEN в Render → добавь в Settings → Environment")
        return

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    print("🚀 Telegram бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    Thread(target=run_telegram).start()
    port = int(os.environ.get("PORT", 5000))
    print(f"🌐 Flask сервер запущен на порту {port}")
    app.run(host="0.0.0.0", port=port)
