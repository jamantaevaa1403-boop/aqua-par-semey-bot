from flask import Flask
import threading
from bot import main as start_bot  # <-- Импорт функции запуска бота

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Aqua Par Semey bot is running!"

def run_bot():
    start_bot()

if __name__ == '__main__':
    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Запускаем Flask-сервер
    app.run(host='0.0.0.0', port=5000)
