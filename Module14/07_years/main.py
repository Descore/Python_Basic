# TODO здесь писать код

def amount(N):
    for i in range(4):
        num = N % 10
        N //= 10
        if i == 0:
            n1 = num
        elif i == 1:
            n2 = num
        elif i == 2:
            n3 = num
        elif i == 3:
            n4 = num

    if ((n1 == n2 == n3) or (n1 == n2 == n4) or (n1 == n3 == n4) or (n2 == n3 == n4)):
        return True
    else:
        return False

def main():
    logic = False

    first_year = int(input('Введите первый год: '))
    second_year = int(input('Введите второй год: '))

    if (first_year < 1000) or (first_year > 10000) or (second_year < 1000) or (second_year > 10000):
        print('Введено некорректное число \n')
        main()
        return 0

    print('\n Года от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')
    for i in range(first_year, second_year):
        logic = amount(i)
        if logic == True:
            print(i)
main()