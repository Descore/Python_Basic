# TODO здесь писать код

first_list = []
second_list = []

j, i = 0, 0

for i in range(3):
    first_list.append(input('Введите ' + str(i+1) + ' число для первого списка: '))

for i in range(7):
    second_list.append(input('Введите ' + str(i+1) + ' число для второго списка: '))

print('Первый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

for i in first_list:
    while first_list.count(i) > 1:
        first_list.remove(i)

print('Новый первый список с уникальными элементами:', first_list)