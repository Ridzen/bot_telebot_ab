""" Тут происходит основная логика бота """

from config.replies_kg import keyboard_kg
from config.rus_ver.callbacks import *
import telebot
from config.config import TOKEN


TOKEN = TOKEN

TOKEN = TOKEN
bot = telebot.TeleBot(TOKEN)

welcome_text = welcome_text


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    file = open('photo_collection\main_photo.jpg', 'rb')
    if message.text.lower() == "привет" or message.text.lower() == "start" or message.text.lower() == "/start":
        bot.send_photo(message.chat.id, file, welcome_text, reply_markup=welcome_msg_markups)
    elif message.text.lower() == wlc_btn_1 or message.text.lower() == "Русский язык":
        bot.send_message(message.chat.id, text='Чем могу я вам помочь?', reply_markup=keyboard_ru)
    elif message.text.lower() == wlc_btn_2 or message.text.lower() == "кыргыз тили":
        bot.send_message(message.chat.id, text='Чем могу я вам помочь?', reply_markup=keyboard_kg)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    handle_callback(bot, call, mobile_banking, bank_card, payment_account, credit, menu_markup)