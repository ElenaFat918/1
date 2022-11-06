import csv

# def read_csv(list):  #
#     '''показать все контакты'''
#     contacts_book = []
#     with open("сontacts.csv", "r", encoding="utf8") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for line in csv_reader:
#             contacts_book.append(client_id=0, family = line[0], 
#             first_name=line[1], last_name=line[2], phone = "+" + line[3])
#             res = list(contacts_book)
#     return res


def read_csv(list):
    with open(
        "C:\gitEduc\pythonapp\HomeWork9_phonebook_bot.py\сontacts.csv",
        encoding="utf8",
    ) as file:
        file_csv = csv.reader(file, delimiter=";"'/n')
        res = list(file_csv)
    return res

def get_contact(item, cursor):
    '''поиск записи'''
    cursor.execute(f"select * from phone where surname like '%{item}%'"
                   f"or name like '%{item}%'")
    results = cursor.fetchall()
    if results:
        return results
    return 'Контакт не найден'

# def add_contact(data, conn, cursor):
#     '''добавить контакт'''
#     name, surname, telephone = data
#     cursor.execute(
#         f"insert into phone (name, surname, telephone, description) "
#         f"values ('{name}', '{surname}', {telephone}, '')")
#     conn.commit()

def add_info(list):  
    with open(
        "C:\gitEduc\pythonapp\HomeWork9_phonebook_bot.py\сontacts.csv",
        "a",
        encoding="utf8",
        newline="",
    ) as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(list)


# def delete(id, conn, cursor):
#     '''Удалить контакт'''
#     try:
#         cursor.execute(
#             f"delete from phone where id={id}"
#         )
#         conn.commit()
#         return 'Контакт был успешно удален'
#     except:
#         return 'Контакт не найден. Попробуйте еще раз'
def del_info(index): 
    '''Удалить контакт'''
    list_csv = read_csv()
    del list_csv[index]
    with open(
        "C:\gitEduc\pythonapp\HomeWork9_phonebook_bot.py\сontacts.csv",
        "w",
        encoding="utf8",
        newline="",
    ) as f:
        writer = csv.writer(f, delimiter=";")
        for row in list_csv:
            writer.writerow(row)