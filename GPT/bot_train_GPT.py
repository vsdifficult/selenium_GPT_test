import telebot
from ChatterBotmaster.chatterbot import ChatBot
from ChatterBotmaster.chatterbot.trainers import ChatterBotCorpusTrainer

# Создаем экземпляр бота
bot = ChatBot('6081937213:AAEzBhI5QaK11mHx1mStYmmshCdPm5Nzuv4')


trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

telegram_bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
tb = telebot.TeleBot(telegram_bot_token)


@tb.message_handler(commands=['start'])
def send_welcome(message):
    tb.reply_to(message, 'Привет! Я телеграм-бот с искусственным интеллектом.')


@tb.message_handler(func=lambda message: True)
def echo_all(message):
    response = bot.get_response(message.text)
    tb.reply_to(message, response)


tb.polling()