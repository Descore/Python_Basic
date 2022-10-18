import random

orig_list = [random.randint(1, 100) for i in range(10)]
#orig_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
edit_list = []
print('Оригинальный список:', orig_list)

def first_version():
    for i in range(0, len(orig_list), 2):
        edit_list.append(tuple(orig_list[i:i+2]))
    print('Новый список: ', edit_list)

def second_version():
    first_half = [i for i in range(0, len(orig_list), 2)]
    sec_half = [i for i in range(1, len(orig_list), 2)]
    edit_list = list(zip(first_half, sec_half))
    print('Новый список:', edit_list)


first_version()
#second_version()