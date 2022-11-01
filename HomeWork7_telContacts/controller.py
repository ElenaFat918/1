import  model # конроллер работает смоделью и интерфейсом поль-ля
import view

def run():
    start = view.begin_menu()
    if start == '1':                # 1 - Посмотреть контакты на экране
        res = model.read_txt()      #   открывает сontacts.txt
        print(res)
           

    elif start == '2':              # 2 - Сохранить контакты в формате txt
        res = model.read_txt()
        model.save_txt(res)         #   сохраняет в save_сontacts.txt
        
    
    elif start == '3':              #   3 - Сохранить контакты в формате csv
        res = model.read_txt()
        model.save_csv(res)         #   сохраняет в save_сontacts.csv
        

    elif start == '4':                       # 4 - Посмотреть контакты на экране в формате csv
        res_csv = model.read_csv()           #   сохраняет в save_сontacts.csv
        print(res_csv)


    elif start == '5':                      # 5 - Сохранить контакты из формата csv в csv
        res =  model.read_csv()
        view.show_result(res)
        model.save_from_csv_to_csv()        #   сохраняет в сontacts.csv
        

    elif start == '6':              # '6 - Сохранить контакты из формата csv в txt
        res = model.read_csv()
        view.show_result(res)
        model.save_from_csv_to_txt()    #   сохраняет в save_сontacts.txt