from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='2learand')],
                                     [KeyboardButton(text='Contacte'),
                                      KeyboardButton(text='despreNoi')]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Apasa un buton de mai jos')

catalog = InlineKeyboardMarkup(inline_keyboard=[
          [InlineKeyboardButton(text='Restaurant', callback_data = 'restaurants')],
          [InlineKeyboardButton(text='Vinarii', callback_data= 'winery')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Transmiteti numarul dvs de telefon', 
                                                           request_contact=True)]],
                                resize_keyboard=True)