from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseShopItem(StatesGroup):
    ChooseItem = State()