import telebot
import os
from dotenv import load_dotenv

# environment variables defined inside a .env file
load_dotenv()
TELEBOT_TOKEN = os.getenv('TELEBOT_TOKEN')
bot = telebot.TeleBot(TELEBOT_TOKEN)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Hey":
        bot.send_message(message.from_user.id, "Hey! How are you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Say 'Hey'!")
    else:
        bot.send_message(message.from_user.id, "I don't understand you, say /help.")


bot.polling(none_stop=True, interval=0)
