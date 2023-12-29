import os

print('Succesfully runed script2')

command = "pip install telebot"
command = "pip install --upgrade pip"
command = "pip install discord.py"
command = "pip install disnake"

res = os.system(command)

print('Все библиотеки успешно обновлены!')