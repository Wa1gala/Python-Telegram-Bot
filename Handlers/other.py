from aiogram import types, Dispatcher
from create_bot import dp
import  json, string




''' 
@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Мат')
        await message.delete()
'''
