from statistics import mode   
import  model_sum as model # конроллер работает смоделью и интерфейсом поль-ля
import view

def button_click(): # Метод обеспечивающий нажатие кнопки
    value_a = view.get_value()  # описываем метод в view
    value_b = view.get_value()
    model.init(value_a, value_b)    # инициализация начальных значений, нужных для модели
    result = model.do_it()
    view.view_data(result, "result")