from aiogram import F,Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.request as rq



router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer("Salut! Aici poti gasi locurile ce poti sa le vizitezi!", reply_markup=kb.main)
    

@router.message(F.text == 'Categorii')
async def catalog(message: Message):
    await message.answer('Alege una dintre categoriile de mai jos', reply_markyp = await kb.categories())

@router.callback_query(F.data.startswitch('category_'))
async def category(callback: CallbackQuery):
    await callback.answer("Ati ales categoria")
    await callback.message.answer('Alegeti unde mai departe?', 
                                  reply_markup=await kb.items(callback.data.split('_')[1]))



@router.message(F.text)
async def understand(message:Message):
    await message.answer('Nu inteleg, incearca te rog sa scrii comanda /start')
