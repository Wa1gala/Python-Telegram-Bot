from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/вк')
b2 = KeyboardButton('/инст')
b3 = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.insert(b3).row(b1, b2)
