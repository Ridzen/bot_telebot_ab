# Основная логика
from config.bot_logic import bot

if __name__ == '__main__':
    bot.polling(none_stop=True)
