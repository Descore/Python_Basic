# TODO здесь писать код
first_class = []
second_class = []

for i in range(160, 177, 2):
    first_class.append(i)

for i in range(162, 181, 3):
    second_class.append(i)

first_class.extend(second_class)

first_class.sort()

print('Отсортированный список учеников: ', first_class)