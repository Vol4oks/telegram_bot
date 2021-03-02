import config #тут лежит токен
import telebot  # pip install telebot
from telebot import types # pip install pyTelegramBotAPI

bot = telebot.TeleBot(config.token)

# Обоработка команд для старта 
@bot.message_handler(commands=['go', 'start']) 
def welcome(message):
    '''
    sti = open(path+'stiker.tgs', 'rb') #нужно добавить картинку в дериктрорию 
    bot.send_sticker(message.chat.id, sti)
    '''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton('Прил')
    item2 = types.KeyboardButton('Мероприятия')
    item1 = types.KeyboardButton('О нас')

    markup.add(item1, item2, item3)

    bot.send_message(
        message.chat.id, 
        'Добро пожаловать, {0.first_name}!\\n\\ Я - <b>{1.first_name}</b>'
        'Просто узнать что-то о нас или пообщаться.\\n\\n'.format(message.from_user, bot.get_me()), 
        parse_mode='html', reply_markup=markup
    )







# Запуск
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print('Непридвиденная ошибка: ', r)
    finally:
        print('Здесь все закончилось')