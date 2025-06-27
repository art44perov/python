from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен вашего бота (замените на ваш реальный токен)
TOKEN = "7007244912:AAEEjeOF0An_zXdyiHeXRNeYucEW1CbPbYg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет сообщение при получении команды /start"""
    await update.message.reply_text("Hello World")

def main():
    """Запуск бота"""
    # Создаем приложение и передаем токен
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
