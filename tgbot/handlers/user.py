from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline.main_menu import main_menu
from tgbot.models.user_commands import UserCommands

user_comm = UserCommands()


async def user_start(message: Message):
    await user_comm.add_new_user()
    await message.answer("Hello, user! It's me okolo official bot! Please choose what you want)", reply_markup=main_menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
