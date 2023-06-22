from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(
    'Автосалон 🚘', callback_data='btn1_data'
)

btn2 = InlineKeyboardButton(
    'Аренда катеров и яхт 🛥', callback_data='btn2_data'
)

btn3 = InlineKeyboardButton(
    'Твои новые кроссы 👟', callback_data='btn3_data'
)

btn4 = InlineKeyboardButton(
    'Оставить отзыв', callback_data='btn4_data'
)

main_menu.add(btn1)
main_menu.add(btn2)
main_menu.add(btn3)
main_menu.add(btn4)
