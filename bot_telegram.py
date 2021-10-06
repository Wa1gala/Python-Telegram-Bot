from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print('Бот вышел в олайн!')

from handlers import client, admin, other

client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



'''
   if message.text == 'Привет':     
        await bot.send_message(message.from_user.id, 'привет')
    else: 
        await bot.send_message(message.from_user.id, message.text)
''' 
