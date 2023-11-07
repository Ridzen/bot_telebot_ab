from telebot import types

welcome_text = ("Здравствуйте!\nВас приветсвует телеграмм бот - Айыл Банк, \n"
                "который ответит на ваши вопросы.\n"
                "Пожалуйста выберите язык, нажав на кнопку 👇 внизу: \n"
                "🔍 Русский язык - 1 \n"
                "🔍 Кыргыз Тили - 2 \n"
                "🔍 English Language - 3 \n")

# Привественные сообщения с ссылками
welcome_msg_markups = types.InlineKeyboardMarkup(row_width=3)  # кнопки под welcome_text
wlc_btn_1 = types.InlineKeyboardButton(text="1", callback_data="wlc_0_ru")
wlc_btn_2 = types.InlineKeyboardButton(text="2", callback_data="wlc_1_ru")
wlc_btn_3 = types.InlineKeyboardButton(text='3', callback_data="wlc_2_en")
welcome_msg_markups.add(wlc_btn_1, wlc_btn_2, wlc_btn_3)

# Вызов слов, по главному меню Ру
keyboard_ru = types.InlineKeyboardMarkup(row_width=2)  # кнопки под сообщением чем я могу вам помочь?
btn_1 = types.InlineKeyboardButton(text="Мобильный банкинг", callback_data="1_ru")
btn_2 = types.InlineKeyboardButton(text="Как получить банковскую карту?", callback_data="2_ru")
btn_3 = types.InlineKeyboardButton(text="Как открыть счёт в банке?", callback_data="3_ru")
btn_4 = types.InlineKeyboardButton(text="Кредиты", callback_data="4_ru")
btn_5 = types.InlineKeyboardButton(text="Филлиалы", callback_data="5_ru")
keyboard_ru.add(btn_1, btn_2, btn_3, btn_4, btn_5)

# Возвращение в главное меню
menu_markup = types.InlineKeyboardMarkup(row_width=1)  # кнопка возврата в меню
menu_btn_1 = types.InlineKeyboardButton(text="Вернуться в основное меню", callback_data="menu_btn_ru")
menu_markup.add(menu_btn_1)

# Ключевые перменные с текстом под страницу 1_ru
mobile_banking = "Тут что по мобильному банкингу"
bank_card = 'Тут что-то по банковской карте'
payment_account = 'Что-то по информации как открыть банковский счет'
credit = 'Что-то по информации как открыть кредит'
fillial = ('Предлагаем вам ознакомится с расписанием работ филлиалов на нашем офицальном сайте💎 \n '
           'https://www.ab.kg/affiliates')

