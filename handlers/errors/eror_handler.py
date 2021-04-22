import logging
from aiogram.utils.exceptions import (
    Unauthorized, InvalidQueryID, TelegramAPIError,
    CantDemoteChatCreator, MessageNotModified,
    MessageToDeleteNotFound, MessageTextIsEmpty,
    RetryAfter, CantParseEntities,
    MessageCantBeDeleted
)

from loader import dp


@dp.errors_handlers()
async def errors_handler(update, exception):
    """

    :param update:
    :param exception:
    :return:
    """
    if isinstance(exception, CantDemoteChatCreator):
        logging.debug("Can't demote chat creator\nНевозможно понизить уровень создателя чата ")
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug('Message is not modified \nСообщение не изменено')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.debug('Message cant be deleted \nСообщение не может быть удалено')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.debug('Message to delete not found \nУдаляемое сообщение не найдено ')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('Message text is empty \nТекст сообщения пуст')
        return True

    if isinstance(exception, Unauthorized):
        logging.info(f'Unauthorized(Несанкционированный): {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f'Invalid query id (Неверный идентификатор запроса): {exception}\n'
                          f'Update(Обновление): {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'Telegram API Error(Ошибка Telegram API ): {exception}\n'
                          f'Update(Обновление): {update}')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'Retry after(Повторить попытку): {exception}\n'
                          f'Update(Обновление): {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'Cant parse entities: {exception}\n'
                          f'Update(Обновление): {update}')
        return True

    logging.exception(f'Update(Обновление): {update} \n{exception}')
