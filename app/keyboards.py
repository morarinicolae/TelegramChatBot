from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)


from aiogram.utils.keyboard import InlineKeyboardBuilder


from app.database.request import get_categories, get_category_item

from .. import logging_config


logger = get_logger(__name__)

logger.info("A initializat ReplyKeyboardMarkup")
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Categorii')],
                                     [KeyboardButton(text='Contacte')],
                                     [KeyboardButton(text='Despre Proiect'),]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Apasa un buton de mai jos')
logger.info("A inceput ")
# catalog = InlineKeyboardMarkup(inline_keyboard=[
#           [InlineKeyboardButton(text='Restaurant', callback_data = 'restaurants')],
#           [InlineKeyboardButton(text='Vinarii', callback_data= 'winery')]])


# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Transmiteti numarul dvs de telefon', 
#                                                            request_contact=True)]],
#                                 resize_keyboard=True)


async def categories():
    all_categories = await get_categories()
    logger.info(f"s-a obtinut categoriile: {all_categories}")
    keyboard = InlineKeyboardBuilder()
    logger.info("A initializat InlineKeyboardBuilder")
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text="Menu principal", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_item(category_id)
    logger.info(f"s-a obtinut categoriile: {all_items}")
    keyboard = InlineKeyboardBuilder()
    logger.info("A initializat InlineKeyboardBuilder")
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text="Menu principal", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()