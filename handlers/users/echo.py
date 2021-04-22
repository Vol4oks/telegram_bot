from aiogram import types
from loader import dp, bot


@dp.message_handler()
async def bot_echo(message: types.Message):
    # Получим chat_id и text
    chat_id = message.chat.id
    text = message.text

    await bot.send_message(chat_id=chat_id, text=text)
