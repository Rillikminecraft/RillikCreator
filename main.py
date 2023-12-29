import telebot 
import os
from telebot import types 

bot = telebot.TeleBot('')

@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, 'тут всё тестовое')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('✅ Создать бота')
    btn2 = types.InlineKeyboardButton('⚠️ Конструктор')
    btn3 = types.InlineKeyboardButton('🌍 Хост')
    btn4 = types.InlineKeyboardButton('🔒 Ваш бот на наш хост')
    btn5 = types.InlineKeyboardButton('🟡 GitHub')
    btn6 = types.InlineKeyboardButton('💻 Тех.Поддержка')
    btn7 = types.InlineKeyboardButton('Скрипты (beta)')
    keyboard_markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, 'Вы запустили бота 💎! Выберите действие кнопкой ниже\nCreated By: @CrashPack1777', reply_markup=keyboard_markup)

@bot.message_handler(content_types=['text'])
def host(message):
    if message.text == "🌍 Хост":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton(' 🔷Бесплатный хост', url='https://replit.com'))
        markup.add(types.InlineKeyboardButton('💻 Наш хост', url='https://telegra.ph/Hosting-v-RillikCreator-12-27'))
        bot.send_message(message.chat.id, 'Конечно! Вот список хостов!', reply_markup=markup)
    if message.text == "✅ Создать бота":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('BotFather', url='https://t.me/BotFather'))
        markup.add(types.InlineKeyboardButton('Пример кода', url='https://telegra.ph/Primery-koda-na-telebot-ot-RillikCreator-12-27'))
        bot.send_message(message.chat.id, 'Вот помощь по созданию бота (коечто о кодинге есть в "Пример кода")', reply_markup=markup)
    if message.text == "🔒 Ваш бот на наш хост":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('Информация', url='https://telegra.ph/Informaciya-o-hoste-na-RillikCreator-12-27'))
        markup.add(types.InlineKeyboardButton('Подключить', url='https://telegra.ph/Hosting-v-RillikCreator-12-27'))
        bot.send_message(message.chat.id, 'Конечно! Вот наш хост и инфа о нём!', reply_markup=markup)
    if message.text == "⚠️ Конструктор":
        bot.send_message(message.chat.id, 'К сожалению конструктор пока не работает, но вы можете написать владельцу он за небольшую сумму зделает вам бота')
    if message.text == "🟡 GitHub":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('🟡 GitHub', url='https://github.com/Rillikminecraft'))
        bot.send_message(message.chat.id, 'GitHub по кнопке ниже', reply_markup=markup)
    if message.text == "💻 Тех.Поддержка":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Владелец', url='https://t.me/CrashPack1777'))
        bot.send_message(message.chat.id, 'Конечно! Тех.поддержка по кнопке ниже', reply_markup=markup)
    if message.text == "Скрипты (beta)":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Скрипты (лист)', callback_data="scripts"))
        markup.add(types.InlineKeyboardButton('Информация о скриптах', url='https://telegra.ph/Skripty-v-RillikCreator-12-29'))
        bot.send_message(message.chat.id, 'Вот всё о скриптах', reply_markup=markup)
    if message.text == "Construkter":
        os.system('python construkter.py')
        bot.send_message(message.chat.id, 'Вы успешно запустили конструктор')
    if message.text == "/script3":
        os.system('python script3.py')
    if message.text == "/script2":
        os.system("python scriptTWO.py")
        bot.send_message(message.chat.id, 'Скрипт выполнен\nБиблиотеки успешно обновлены!')
    if message.text == "/script1":
        os.system("python scriptONE.py")
        bot.send_message(message.chat.id, 'Скрипт выполнен')
    if message.text == "/BebraLoaderSTART12213":
        os.system("python BebraLoader.py")
        bot.send_message(message.chat.id, 'бебра бот запущен')
    if message.text == "sms v chat":
                id_tg_ = str(message.from_user.id)
    TO_CHAT_ID = "-4029275824"
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id) 

@bot.callback_query_handler(func=lambda call: True)
def scriptscallback(call):
    try:
        if call.message:
            if call.data == "scripts":
                bot.send_message(call.message.chat.id, "/script1 - тестовый скрипт\n/yb(код) - включает/выключает вашего бота (одобреного и подключеного)")
    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['officialbot', 'ob'])
def officialbot(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('1. Bebra', url='https://t.me/TestPy1234234Bot'))
    bot.send_message(message.chat.id, 'Конечно! Вот список наших ботов помимо этого!')

bot.polling(none_stop=True)