import imp  


import data_provider as prov    #   импортируем данные из модуля data_provider
import logger as log            #   импортируем данные из модуля logger

def temperature_view(sensor):
    data = prov.get_temperature(sensor) #   забираем данные из data_provider, вызывая соовет метод
    log.temperature_logger(data)        #   записываем в лог инф с полученным значением 
    return data                         #   возвращаем это значение


def pressure_view(sensor):
    data = prov.get_preassure(sensor)
    log.pressure_logger(data)
    return data

    
def wind_speed_view(sensor):
    data = prov.get_wind_speed(sensor)
    log.wind_speed_logger(data)
    return data

    