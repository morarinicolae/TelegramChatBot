from aiogram import F,Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Salut!", reply_markup=kb.main)
    await message.reply("Cum te simti?")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Cu ce va pot ajuta?')

@router.message(F.text == 'Catalog')
async def understand(message:Message):
    await message.answer('Alegeti categoriile din catalogul nostru', reply_markup=kb.catalog)

@router.callback_query(F.data == 'restaurants')
async def restaurants(callback: CallbackQuery):
    await callback.answer('Dvs ati ales categoria')
    await callback.message.answer('Dvs Ati ales restaurante, uitati mai jos cateva din ele')

#Inregistrarea userului
@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Introduceti numele:')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Register.age)
    await message.answer('Introduceti varsta:')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Register.number)
    await message.answer('Introduceti numarul dvs de telefon:', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Numele dvs: {data["name"]}\n Varsta dvs: {data["age"]}\n Numarul dvs: {data["number"]} ')
    await state.clear()



@router.message(F.text)
async def understand(message:Message):
    await message.answer('Nu inteleg, incearca te rog sa scrii comanda /start')
