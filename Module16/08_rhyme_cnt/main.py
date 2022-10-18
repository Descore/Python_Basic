# TODO здесь писать код

people_list = []
i_num, num_remove = 0, 0

people = int(input('Кол-во человек: '))
num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', num, 'человек')

for i in range(1, people+1):
    people_list.append(i)

while True:
    print('\nТекущий круг людей', people_list)
    print('Начало счёта с номера', people_list[i_num])
    num_remove = (i_num + num % len(people_list)) - 1
    print('Выбывает человек под номером', people_list[num_remove])
    people_list.pop(num_remove)
    i_num = num_remove % len(people_list)

    if len(people_list) == 1:
        print('\nОстался человек под номером', people_list[0])
        break
