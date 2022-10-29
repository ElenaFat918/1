import imp
from random import randint  #ВОСПОЛЬЗ генератором псевдо-случ чисел

def get_temperature(sensor):    # получение измерений с датчиков, опишем например sensor
    return randint(-20, 0) if sensor else randint(0, 20)


def get_preassure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)


def get_wind_speed(sensor): 
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)

def data_collection(sensor = 1):    # собирает кортеж из данных
    return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))