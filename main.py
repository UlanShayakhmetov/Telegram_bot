import requests
from pprint import pprint
from config import open_weather_token
import datetime


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
    # pprint(data)
    except Exception as ex:
        print(ex)
        print("Check your errror")

    city = data["name"]
    cur_weather = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

    print(
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"The weather in the city: {city}\nTemperature: {cur_weather}C°\n"
        f"Humidity: {humidity}%\nPressure: {pressure} hpa\nWind:{wind} m/s\n"
        f"Sunrise: {sunrise}"
    )


def main():
    city = input("Enter your city: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
