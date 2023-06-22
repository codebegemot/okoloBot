from sqlalchemy import and_

from tgbot.models.models import ShopCategories, ShopItems, db



class ShopCommands:

    async def get_shop_categories(self):
        categories = await ShopCategories.query.gino.all()
        return categories

    async def total_category_items(self, category_id) -> int:
        total = await (db.select([db.func.count()])
                       .where(ShopItems.category_id == category_id)
                       .gino
                       .scalar())
        return total

    async def get_item(self, item_id):
        item = ShopItems.query.where(ShopItems.id == item_id).gino.first()
        return item

    async def get_items(self, category_id, items_per_page, start_index):

        items = await ShopItems.query.where(ShopItems.category_id == category_id).limit(items_per_page).offset(
            start_index).gino.all()
        return items
