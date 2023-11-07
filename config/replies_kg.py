from telebot import types

# Ключевые слова
keyboard_kg = types.InlineKeyboardMarkup(row_width=1) #кнопки под сообщением чем я могу вам помочь?
btn_1 = types.InlineKeyboardButton(text="Мобильный банкингы", callback_data="1_kg")
btn_2 = types.InlineKeyboardButton(text="Как получить банковскую мен алды?", callback_data="2_kg")
btn_3 = types.InlineKeyboardButton(text="Как открыть счёт в банке?", callback_data="3_kg")
btn_4 = types.InlineKeyboardButton(text="Кредиты", callback_data="4_kg")
keyboard_kg.add(btn_1, btn_2, btn_3, btn_4)
