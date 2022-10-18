phonebook = {}

def action():
    print('\n Выберите номер действия: \n 1. Добавить контакт \n 2. Найти человека \n')
    num_action = int(input())
    if num_action == 1:
        add_contact()
    elif num_action == 2:
        find_contact()
        pass
    else:
        action()
        return 0


def add_contact():
    fio = (input('Введите имя и фамилию нового контакта (через пробел): ')).split()
    phone_num = int(input('Введите номер телефона: '))
    for k, v in phonebook.items():
        if (k[0].lower() == fio[0].lower()) and (k[1].lower() == fio[1].lower()):
            print('Такой человек уже есть в контактах.')
    else:
        phonebook.update({tuple(fio): phone_num})
    print('Текущий словарь контактов:', phonebook)
    action()
    return 0

def find_contact():
    last_name = input('Введите фамилию: ')
    for k, v in phonebook.items():
        if k[1].lower() == last_name.lower():
            print(k[0], k[1], v)
            break
    else:
        print('Такого человека нет в контактах')
    action()
    return 0

action()
