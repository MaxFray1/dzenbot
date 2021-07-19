# from flask import Flask
# from flask_sslify import SSLify


# app = Flask(__name__)
# sslify = SSLify(app)

# @app.route('/')
# def index():
#     return '<h1>Test flask app</h1>'

# if __name__ == '__main__':
#     app.run()

#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types

API_TOKEN = '1949484698:AAFkkfN586lV2NjFDu6XBcegj_nN6g7T7q8'

bot = telebot.TeleBot(API_TOKEN)

def myKeyboard(count=0, btn1_text="", cb_data1="", btn2_text="", cb_data2=""):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(btn1_text, callback_data=cb_data1)
    markup.add(btn1)
    if(count == 2):
        btn2 = types.InlineKeyboardButton(btn2_text, callback_data=cb_data2)
        markup.add(btn2)
    return markup

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    text = "Привет это ДзенБот!!! Хочешь получить бесплатный урок?"
    keyboard = myKeyboard(2,'Да', 'Yes1', 'Нет', 'No1')
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = "Хочешь подарок?"
    keyboard = myKeyboard(1,'Да','Yes0')
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Yes1':
            text1 = "Ты подписан на Ваню???"
            keyboard = myKeyboard(2,'Да', 'Yes2', 'Нет', 'No2')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'No1':
            text1 = "Ты упустил свой шанс заработать миллион рублей, лох"
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML')
        elif call.data == 'Yes2':
            text1 = 'Вот твоя ссылка: [http://ссылка.хрю/322qwerty](https://www.youtube.com/watch?v=dQw4w9WgXcQ)'
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='Markdown')
        elif call.data == 'No2':
            text1 = "Скорее подпишись на Ваню!!!"
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton('Инста Вани', url='https://www.instagram.com/funtik_iv/')
            keyboard.add(btn1)
            btn2 = types.InlineKeyboardButton('Подписался!!!', callback_data='Yes2')
            keyboard.add(btn2)
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text=text1, parse_mode='HTML', reply_markup=keyboard)
        elif call.data == 'Yes0':
            text1 = "Ты подписан на Ваню???"
            keyboard = myKeyboard(2,'Да', 'Yes2', 'Нет', 'No2')
            bot.delete_message(call.message.chat.id, call.message.id)
            bot.send_message(call.message.chat.id, text1, parse_mode='HTML', reply_markup=keyboard)
        
bot.polling()