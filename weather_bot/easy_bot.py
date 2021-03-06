import telebot
from telebot import types
from prediction import get_prediction

bot = telebot.TeleBot('1769995853:AAGJ45pcByH14_09sSfHVTKolj8Z7Wl8ibw')

#Метод для обработки комманд
@bot.message_handler(commands = ['start', 'help'])
def welcome(message):
    #добавим клавиатуру
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        key_temp = types.InlineKeyboardButton(text='Температура', callback_data='temp')
        keyboard.add(key_temp) #добавляем кнопку в клавиатуру
        key_wind = types.InlineKeyboardButton(text='Ветер', callback_data='wind')
        keyboard.add(key_wind)
        key_tempwind = types.InlineKeyboardButton(text='Температура и Ветер', callback_data='tempwind')
        keyboard.add(key_tempwind)
        bot.send_message(message.from_user.id, 'Добрый день! Что бы вы хотели узнать?', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Пожалуйста, напечатайте /start')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    prediction = get_prediction(call.data)
    if type(prediction) != str:
        prediction = prediction[0] + ' и ' + prediction[1]
    bot.send_message(call.from_user.id, 'В Москве сегодня ' + prediction)

bot.polling()