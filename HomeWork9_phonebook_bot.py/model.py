import csv

def read_csv():
    with open(
        "C:\gitEduc\pythonapp\StudyTelegramBot.py\сontacts.csv",
        encoding="utf8",
    ) as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res

def find(surname):
    sp = []
    list_csv = read_csv()
    for i, row in enumerate(list_csv):  # поиск по строкам и столбцам 
        if row[0] == surname:       # ищим в нулевом столбце нужную фымилию
            sp.append(row)      #   записываем строку с данной фамилией
    return sp
    
def add_info(list):  
    with open(
        "C:\gitEduc\pythonapp\StudyTelegramBot.py\сontacts.csv",
        "a",
        encoding="utf8",
        newline="",
    ) as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(list)

def del_info(index): 
    '''Удалить контакт'''
    list_csv = read_csv()
    del list_csv[index]
    with open(
        "C:\gitEduc\pythonapp\StudyTelegramBot.py\сontacts.csv",
        "w",
        encoding="utf8",
        newline="",
    ) as f:
        writer = csv.writer(f, delimiter=";")
        for row in list_csv:
            writer.writerow(row)