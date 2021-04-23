from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# Кастомный фильтр на Приватный чат с ботом
class IsPrivate(BoundFilter):

    # Функция используется каждый раз когда приходит апдейт,
    # и диспатчер проходит по всем хендлурам и фильтрам, используемых в них
    # Этот фильтр мы будем использовать только для message_handler,
    # и типа Message
    async def check(self, message: types.Message):
        #
        return message.chat.type == types.ChatType.PRIVATE
