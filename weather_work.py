import json

import requests

import argparse

import datetime

api_key = '5e57c5a0225dc6b1cfb20be3a829b0bf'
parser = argparse.ArgumentParser(description = 'Прогноз погоды города на три дня')
parser.add_argument('city', help = 'Город')
city = parser.parse_args().city

response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&lang=ru&units=metric&appid={api_key}')
data = json.loads(response.text)

day_1 = data['list'][0]['dt_txt']
day_x = datetime.datetime.strptime(day_1, '%Y-%m-%d %H:%M:%S')
day_2 = day_x + datetime.timedelta(days = 1)
day_2 = day_2.strftime("%Y-%m-%d 15:00:00")
day_3 = day_x + datetime.timedelta(days = 2)
day_3 = day_3.strftime("%Y-%m-%d 15:00:00")

for i in data['list']:
	desc = i['dt_txt'],i['main']['temp'],i['weather'][0]['description']
	if i['dt_txt'] == day_1:
		print(desc)
	elif i['dt_txt'] == day_2:
		print(desc)
	elif i['dt_txt'] == day_3:
		print(desc)
	else:
		pass