import telebot 
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    keyboard_markup = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Функции')
    keyboard_markup.add(btn1)
    markup.add(types.InlineKeyboardButton('Бот бандит', url='https://t.me/banditchatbot'))
    bot.send_message(message.chat.id, 'Бот запущен!\nПерейти в бот бандит: https://t.me/banditchatbot', reply_markup=markup)
    bot.send_message(message.chat.id, 'ID: RillikCreator\nCreated BY: @CrashPack1777', reply_markup=keyboard_markup)

@bot.message_handler(commands=['RillikCreator', 'rc', 'rillikcreator'])
def rillikcreator(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Вот бот', url='https://t.me/RillikCreatorBot'))
    bot.send_message(message.chat.id, 'Конечно! Вот RillikCreator:', reply_markup=markup)

@bot.message_handler(commands=['ad'])
def ad(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Вот список рекламодателей', callback_data="ad"))
    bot.send_message(message.chat.id, 'Конечно! Список партнёров/рекламодателей по кнопке ниже', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def adcallback(call):
    try:
        if call.message:
            if call.data == "ad":
                bot.send_message(call.message.chat.id, "Партнёры не найдены.")
    except Exception as e:
        print(repr(e))

@bot.message_handler(content_types=['text'])
def all(message):
    if message.text == "Функции":
        bot.send_message(message.chat.id, '/ad - партнёры/рекламодатели\n/RillikCreator - очень полезный бот')

print('бот запущен: ID Bebra')

bot.polling(none_stop=True)