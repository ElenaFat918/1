import csv
from re import S


def read_txt():     # 1 - Посмотреть контакты на экране
    with open ('C:\gitEduc\pythonapp\HomeWork7_telContacts\сontacts.txt','r', encoding = 'utf-8') as file:
        res = file.read()
        print(res)
    return res

# res = read_txt()

def save_txt(res):      # 2 - Сохранить контакты в формате txt
    with open('C:\gitEduc\pythonapp\HomeWork7_telContacts\save_сontacts.txt','w', encoding = 'utf-8') as save_txt_file:
        save_txt_file.write(res)
   
# save_txt(txt_file)

def save_csv(res):    # 3 - Сохранить контакты в формате csv
    res = res.replace(' ', ';')
    with open('C:\gitEduc\pythonapp\HomeWork7_telContacts\save_сontacts.csv', "w", encoding='utf-8') as save_csv:
        save_csv.write(res)

# save_csv(txt_file)

def read_csv():     # 4 - Посмотреть контакты на экране в формате csv
    with open('C:\gitEduc\pythonapp\HomeWork7_telContacts\save_сontacts.csv', encoding="utf8") as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res

def save_from_csv_to_csv():     # 5 - Сохранить контакты из формата csv в csv
    with open('C:\gitEduc\pythonapp\HomeWork7_telContacts\save_сontacts.csv', encoding="utf8") as save_csv, open('C:\gitEduc\pythonapp\HomeWork7_telContacts\сontacts.csv', 'w', encoding="utf8", newline='') as csv_to_csv_file:
        reader = csv.reader(save_csv, delimiter=';')
        writer = csv.writer(csv_to_csv_file, delimiter=';')
        for row in reader:
            writer.writerow(row)

# save_from_csv()

def save_from_csv_to_txt():     # '6 - Сохранить контакты из формата csv в txt
    list = read_csv()
    for i in list:
        space = ' '.join(i)
        with open('C:\gitEduc\pythonapp\HomeWork7_telContacts\save_сontacts.txt', "a", encoding='utf-8') as save_txt_in_csv:
            save_txt_in_csv.writelines(space + '\n')
# save_from_csv_to_txt()

# def impotr_csv(data):
#     data = list(el.split(';') for el in data)
#     with open("book_imp.csv", "w", encoding = 'utf-8', newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(data)