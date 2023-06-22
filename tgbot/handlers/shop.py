from aiogram import Dispatcher, types

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, \
    InputMedia
from aiogram.utils.callback_data import CallbackData
from tgbot.keyboards.inline.main_menu import main_menu
from tgbot.models.models import ShopItems
from tgbot.models.shop_commands import ShopCommands

shop_comm = ShopCommands()
get_category = CallbackData('get_category', 'category_id')


async def main_handle(cq: CallbackQuery):
    categories = await shop_comm.get_shop_categories()
    markup = InlineKeyboardMarkup()
    for num, category in enumerate(categories):
        btns = InlineKeyboardButton(text=f'{category.name}', callback_data=f"category_{category.id}")
        markup.add(btns)
    mmBtn = InlineKeyboardButton('⏪ в главное меню', callback_data='main_menu')
    markup.add(mmBtn)
    await cq.message.edit_text("Кроссовки со всего мира в одном магазине.\n"
                               "Доставка по всей России и СНГ.\n"
                               "Выбрать модель:",
                               reply_markup=markup)


async def handle_category_selection(cq: CallbackQuery):
    category_id = int(cq.data.split('_')[1])

    await display_items(cq.message, category_id=category_id, page=1)


async def display_items(message: Message, category_id: int, page: int):
    items_per_page = 1

    total_items = await shop_comm.total_category_items(category_id)

    total_pages = (total_items // items_per_page) + (1 if total_items % items_per_page > 0 else 0)

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    items = await shop_comm.get_items(category_id, items_per_page, start_index)

    text = f"<b>{page}/{total_pages}:\n</b>"

    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = []
    media_group = []
    for item in items:
        text += f"<b>{item.name}</b>\n\n" \
                    f"Размеры: {item.size}\n" \
                    f"Цена: {item.price}\n\n" \
                    f"<i>Доставка по всей России и СНГ.</i>"
        mmBtn = InlineKeyboardButton('Выбрать другой бренд', callback_data='btn3_data')
        buttons.append(mmBtn)
        buy_btn = InlineKeyboardButton('Купить', callback_data=f"buy_{item.id}")
        buttons.append(buy_btn)
        media = InputMediaPhoto(media=item.photo)
        media_group.append(media)

    if page > 1:
        keyboard.insert(InlineKeyboardButton("⬅️", callback_data=f"prev_{category_id}_{page}"))

    if page < total_pages:
        keyboard.insert(InlineKeyboardButton("➡️", callback_data=f"next_{category_id}_{page}"))

    keyboard.add(*buttons)

    await message.answer_media_group(media_group)
    await message.answer(text, reply_markup=keyboard)


async def handle_pagination(cq: CallbackQuery):
    action, category_id, page = cq.data.split('_')
    category_id = int(category_id)
    page = int(page)

    if action == 'prev':
        page -= 1
    elif action == 'next':
        page += 1

    await display_items(cq.message, category_id=category_id, page=page)


async def call_menu(cq: CallbackQuery):
    await cq.message.edit_text("Вы находитесь в главном меню. Рекомендую чекнуть наши новенькие брички 🆕😉",
                               reply_markup=main_menu)


async def call_models_menu(cq: CallbackQuery):
    pass


async def write_admin(cq: CallbackQuery):
    pass


def shop_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(handle_category_selection, lambda call: call.data.startswith('category_'))
    dp.register_callback_query_handler(handle_pagination, lambda call: call.data.startswith(('prev_', 'next_')))

    # dp.register_callback_query_handler(main_handler, lambda call: call.data == "btn1_data", state="*")
    # dp.register_callback_query_handler(main_handler, lambda call: call.data == "btn2_data", state="*")
    dp.register_callback_query_handler(main_handle, lambda call: call.data == "btn3_data", state="*")
    # dp.register_callback_query_handler(main_handler, lambda call: call.data == "btn4_data", state="*")

    dp.register_callback_query_handler(write_admin, lambda call: call.data == "write_admin")
    dp.register_callback_query_handler(call_menu, lambda call: call.data == "main_menu", state="*")
