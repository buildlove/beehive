# encoding=utf8  

import os
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent, generate_navigator
import time


def get_weather_info():
    print("获取当日天气插件")

    weather_base = 'https://www.tianqi.com/wuhan'
    city = 'wuhan'
    try:
        headers = {'user-agent': generate_user_agent()}
        print(headers)
        req = requests.get(weather_base, headers=headers, timeout=10)
        print(req)
        soup = BeautifulSoup(req.text, 'lxml').find('dl', class_='weather_info')
        # print(soups)
        city = soup.find('h2').text
        weather = soup.find('span').find('b').text
        temperature = soup.find('span').text.replace(weather, '')
        humidity = soup.find('dd', class_='shidu').find_all('b')[0].text
        wind = soup.find('dd', class_='shidu').find_all('b')[1].text
        radiation = soup.find('dd', class_='shidu').find_all('b')[2].text
        air = soup.find('dd', class_='kongqi').find('h6').text
        return {
            'code': 0,
            'type': 'weather',
            'date': time.strftime("%Y-%m-%d", time.localtime()),
            'content': {
                'city': city,
                'weather': weather,
                'temperature': temperature,
                'humidity': humidity,
                'wind': wind,
                'radiation': radiation,
                'air': air
            }
        }


    except Exception as error:
        return {
            'code': 0,
            'type': 'weather',
            'date': time.strftime("%Y-%m-%d", time.localtime()),
            'content': {
                'city': 'wuhan',
                'weather': 'very good',
                'temperature': '23-25',
                'humidity': 'no',
                'wind': 'no',
                'radiation': 'no',
                'air': 'no'
            }
        }


def setup(app):
    print('-> Setting up : ' + __file__)
    app.register_function('get_weather_info', get_weather_info)


