from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config

bot = Bot(config.token)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
	chat_id = message.chat.id
	text = ' Тестовый текст'

	await bot.send_message(chat_id=chat_id, text=text)

executor.start_polling(dp)
