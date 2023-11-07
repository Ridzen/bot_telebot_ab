from config.rus_ver.replies_ru import *


def handle_callback(bot, call, mobile_banking, bank_card, payment_account, credit, menu_markup):
    if call.data == "wlc_0_ru":
        bot.send_message(call.message.chat.id, text='Выберите раздел:', reply_markup=keyboard_ru)
    # проверка
    elif call.data == "1_ru":
        bot.send_message(call.message.chat.id, text=mobile_banking, reply_markup=menu_markup)
    elif call.data == "2_ru":
        bot.send_message(call.message.chat.id, text=bank_card, reply_markup=menu_markup)
    elif call.data == "3_ru":
        bot.send_message(call.message.chat.id, text=payment_account, reply_markup=menu_markup)
    elif call.data == "4_ru":
        bot.send_message(call.message.chat.id, text=credit, reply_markup=menu_markup)
    elif call.data == "5_ru":
        bot.send_message(call.message.chat.id, text=fillial, reply_markup=menu_markup)
    elif call.data == 'menu_btn_ru':
        file = open('photo_collection\main_photo.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'С возвращением в главное меню😁! \n'
                                                   'Выберите чем мы можем вам помочь?', reply_markup=keyboard_ru)


