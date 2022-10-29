from user_interface import temperature_view     #   импортируем методы(чтобы не использ библиотеки) из модуля user_interface
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):     #   метод получает в аргументе device = 1(в качетсве демонстрации,
                            #   т/е из первого девайса берется значение)
    style = 'style="font-size:30px;"'   #   стиль в конечном html представлении шрифт 30
    html = '<html>\n  <head></head>\n  <body>\n'    #   заготовка для html представления
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))    #    обычная строка, которая форматируется: в качестве температуры мы вставляем значение этой темп-ры, полученное из view
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:   #   создаем файл index.html
        page.write(html)    #   сохраняем файл index.html

    return html



def new_create(data ,device = 1):   #   создадим метод получения трех измерений в   html представлении, доп аргумент data 
    t, p, w = data                  #   данные о темп давл и скор ветра 
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, t)                           #   вместо явного вызова метода temperature_view указываем t
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '  </body>\n</html>'
    
    with open('new_index.html', 'w') as page:
        page.write(html)

    return data #   возвращаем данные (флюид интерфейс)