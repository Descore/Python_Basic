# TODO здесь писать код

sticks = 10 #int(input('Кол-во палок:'))
throws = 3 #int(input('Кол-во бросков:'))

sticks_list = ['I' for _ in range(sticks)]
result = ''

for i in range(throws):
    print('Бросок', i+1, ': Сбиты палки с номера ', end='')
    L = int(input())
    R = int(input('по номер '))

    for j in range(L-1, R):
        sticks_list[j] = '.'

for i in sticks_list:
    result += i

print('Результат:', result)

