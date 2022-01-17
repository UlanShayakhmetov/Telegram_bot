import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Enter your city")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            f"The weather in the city: {city}\nTemperature: {cur_weather}C°\n"
            f"Humidity: {humidity}%\nPressure: {pressure} hpa\nWind:{wind} m/s\n"
            f"Sunrise: {sunrise}")
    except:
        await message.reply("Check your errror")


if __name__ == '__main__':
    executor.start_polling(dp)
