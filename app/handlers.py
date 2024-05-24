from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Salut! Aici poti gasi locurile ce poti sa le vizitezi!', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer('Alege una dintre categoriile de mai jos', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Ați ales categoria')
    await callback.message.answer('Alegeți un produs după categorie',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Ați ales produsul')
    await callback.message.answer(f'Titlu: {item_data.name}\nDescriere: {item_data.description}\nPreț: {item_data.price}')
