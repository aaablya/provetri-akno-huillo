import logging
import schedule
import time
import threading
import telebot

# соси
TOKEN = ''
CHAT_ID = ''  # соси

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для отправки сообщения
def send_message():
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text="проветри окно хуйло")
    logger.info("хуйло проветривает окно")

# Планируем выполнение функции раз в час
schedule.every().hour.at(":00").do(send_message)

# Функция для запуска планировщика в отдельном потоке
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Запускаем планировщик в отдельном потоке
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

    # Бот будет работать до прерывания
    logger.info("Бот запущен и работает...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Бот остановлен.")
