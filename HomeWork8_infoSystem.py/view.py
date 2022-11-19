# Создать телефонный справочник с возможностью импорта и экспорта данных в
# нескольких форматах (txt, csv, по желанию - json, xml)
# под форматами понимаем структуру файлов, например:в файле на одной строке
# хранится одна часть записи, пустая строка - разделитель

# Создать информационную систему позволяющую
# работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# Примерная функциональность для реализации:
# - получить список всех людей
# - CRUD (create-read-update-delete) для определенного
# человека в БД
# - импортировать / экспортировать людей в БД

def begin_menu():
    print('1 - Посмотреть контакты на экране в формате txt')
    print('2 - Сохранить контакты в формате txt')
    print('3 - Сохранить контакты в формате csv')
    print('4 - Посмотреть контакты на экране в формате csv')
    print('5 - Сохранить контакты из формата txt в csv')
    print('6 - Сохранить контакты из формата csv в txt')
    print('7 - Добавить контакт')
    print('8 - Удалить контакт')
    print('9 - Изменить контакт')
    return input('Введите цифру: ')


def show_result(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))



def add_info():   # 7 - Добавить контакт
    print('Добавляю запись. Введите ФИО и тел через пробел')
    in_info = input().split()
    return in_info



def delete():   # 8 - Удалить контакт
    print('Удаляю запись. Введите индекс для удаления')
    return int(input())


def change_tel():  # 9 - Изменить контакт
    print('Меняю телефон. Введите индекс (начало с 0) для изменения и новый телефон, через Enter')
    return int(input()), input()