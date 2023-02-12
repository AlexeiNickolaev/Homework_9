from aiogram import Bot, Dispatcher, types, executor


async def on_start(_):
    print('Бот запущен!')

bot = Bot('6231134708:AAFcHa4QfZBtpaVetAWVTXG-nyUahx5nxdk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)