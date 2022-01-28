import telebot
import os
from dotenv import load_dotenv
from telebot import types

# environment variables defined inside a .env file
load_dotenv()
TELEBOT_TOKEN = os.getenv('TELEBOT_TOKEN')
bot = telebot.TeleBot(TELEBOT_TOKEN)

name = '';
surname = '';
age = 0;


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'What is your name?');
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Type /reg');


def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'What is your surname?');
    bot.register_next_step_handler(message, get_surname);


def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'How old are you?');
    bot.register_next_step_handler(message, get_age);


def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, '\'int\' only');
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Yep', callback_data='yes');
    keyboard.add(key_yes);
    key_no = types.InlineKeyboardButton(text='No', callback_data='no');
    keyboard.add(key_no);
    question = 'You are ' + str(age) + ', your name is ' + name + ' ' + surname + '?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        print('(:')
        bot.send_message(call.message.chat.id, 'Nice to meet you : )');
    elif call.data == "no":
        print('):')


bot.polling(none_stop=True, interval=0)
