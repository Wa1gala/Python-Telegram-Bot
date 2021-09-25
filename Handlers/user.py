from os import stat
from aiogram import types
from create_bot import dp, bot

'''
@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет': 
        await message.answer('И тебе привет!')
'''
@dp.message_handler(commands=['stat', 'help'])
async def command_start(message: types.Message):
    try:
        await message.answer('Test!')
        await message.delete()
    except: 
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Custom_Walgala_ShopBot')

@dp.message_handler(commands='Мой ВК')
async def my_vk_command(message: types.Message):
    await message.answer('https://vk.com/ffeeskers')

@dp.message_handler(commands='Мой инст')
async def my_inst_command(message: types.Message):
    await message.answer('https://www.instagram.com/alexk.480/')


    

    
   # await message.reply(message.text)
   # await bot.send_message(message.from_user.id, message.text)



