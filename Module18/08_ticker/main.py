# TODO здесь писать код

first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

logic = True

if first_str == second_str:
    print('Первая строка получается из второй со сдвигом 0')
else:
    for i in range(1, len(first_str)+1):
        if first_str[i:]+first_str[:i] == second_str:
            print('Первая строка получается из второй со сдвигом', i)
            logic = False
    if logic:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

