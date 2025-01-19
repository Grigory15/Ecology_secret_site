import time
from random import randint
import telebot
from telebot.types import Message
bot = telebot.TeleBot("7982699133:AAH8JeYX3-D7fgcHJ-MSE2mPdIzqfnh3Ilg")
twenty_one = 0
code = 'решение?'
@bot.message_handler(commands=["start"])
def start_command(message:Message):
    bot.send_message(message.chat.id, 'введите код, доступа (1: "начало")')


@bot.message_handler(content_types=['text'])
def code_cmd(message: Message):

    if message.text.lower() == code:
        time.sleep(2)

        bot.send_message(message.chat.id, 'код правильный')

        time.sleep(1)

        bot.send_message(message.chat.id, 'данная секция еще не доделана')

    elif message.text.lower() == "начало":
        time.sleep(0.25)
        bot.send_message(message.chat.id,'https://riddlemaker.pythonanywhere.com/')
    elif message.text.lower() == "лед":
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'https://riddlemaker.pythonanywhere.com/chal1')
    elif message.text.lower() == "глобальное потепление":
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'https://riddlemaker.pythonanywhere.com/chal2')
    elif message.text.lower() == "углекислый газ":
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'https://riddlemaker.pythonanywhere.com/chal3')
    elif message.text.lower() == "парниковый эффект":
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'https://riddlemaker.pythonanywhere.com/chal4')
    elif message.text.lower() == "углерод":
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'https://riddlemaker.pythonanywhere.com/chal5')
    elif message.text.lower() == "решение проблемы":
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'https://tushkanchik.pythonanywhere.com/')
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'Логин: secret_account@gmail.com')
        time.sleep(0.25)
        bot.send_message(message.chat.id, 'Пароль: Apocalypse')
    elif message.text.lower() == "конец":
        bot.send_message(message.chat.id, 'не будь наивным')
    else:
        bot.send_message(message.chat.id,'error, не верный код доступа')

bot.polling()