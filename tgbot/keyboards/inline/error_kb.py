from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

error_kb = InlineKeyboardMarkup()
admin_btn = InlineKeyboardButton("Написать администратору", callback_data="write_admin")
error_kb.add(admin_btn)