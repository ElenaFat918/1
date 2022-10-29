from datetime import datetime as dt #МОДУЛЬ ЛОГИРОВНИЯ. ВСЕГДА нужно работать с текущ датой
from time import time

def temperature_logger(data):   # записваем в псевдо-ехеle файл
    # time = dt.now().strftime('%H:%M') чтобы получить время обращаемся к модулю dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'    #   логируем время и температуру с переходом на новую строку
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))
