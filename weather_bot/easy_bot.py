import telebot
from telebot import types
from prediction import get_prediction

bot = telebot.TeleBot('1769995853:AAGJ45pcByH14_09sSfHVTKolj8Z7Wl8ibw')

#Метод для обработки комманд
@bot.message.handler(commands = ['start', 'help'])
def welcome(message):
    #добавим клавиатуру
    if message.text == '\start':
        keyboard = types.InlineKeyboardMarkup()
        key_temp = types.InlineKeyboardButton(text='Температура', callback_data='temp')
        keyboard.add(key_temp) #добавляем кнопку в клавиатуру
        key_wind = types.InlineKeyboardButton(text='Ветер', callback_data='wind')
        keyboard.add(key_wind)
        key_tempwind = types.InlineKeyboardButton(text='Температура и Ветер', callback_data='tempwind')
        keyboard.add(key_tempwind)
    elif message.text == '\help':
        bot.send_message(message.from_user.id, 'Пожалуйста, напечатайте \start')


bot.polling()