from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


'''  /start, /help, /вк, /инст   '''
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Test', reply_markup=kb_client)
        await message.delete()
    except: 
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Custom_Walgala_ShopBot')

# @dp.message_handler(commands=['вк'])
async def my_vk_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'https://vk.com/ffeeskers')

# @dp.message_handler(commands=['инст'])
async def my_inst_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'https://www.instagram.com/alexk.480/')



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(my_vk_command, commands=['вк'])  
    dp.register_message_handler(my_inst_command, commands=['инст'])
    