import telebot
import requests
import json

bot = telebot.TeleBot('6786596586:AAGBkY-wdTfjlsK90q7g-RhxXd32cuG-E7U')
API = '71f18886c73c8dedad7af071775b7476'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        data2 = str(data["weather"][0]["description"])
        bot.reply_to(message, f'Сейчас погода в {city} ({data["sys"]["country"]}) {data["main"]["temp"]}°C. {data2.capitalize()}')
    else:
        bot.reply_to(message, 'Город указан не верно')
bot.polling(none_stop=True)
