from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.models.user_commands import UserCommands

user_comm = UserCommands()


async def admin_start(message: Message):
    await user_comm.add_new_user()
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
