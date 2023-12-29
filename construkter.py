import os 
# это только в разработке хз чо там будет
py_file = open("1.py", "w")

py_file.write("import telebot\nfrom telebot import types\n\nbot = telebot.TeleBot('')\n\n@bot.message_handler(commands=['start'])\ndef start(message):\n    bot.send_message(message.chat.id, 'Бот запущен!')")

open("1.py", "w").write("ПОН")

print(os.stat("1.py"))
