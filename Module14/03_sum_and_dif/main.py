# TODO здесь писать код

def sum_n(N):
    plus_n = 0
    while N != 0:
        plus_n += N % 10
        N = N // 10
    return plus_n

def amount(N):
    plus_n = 0
    while N != 0:
        plus_n += 1
        N = N // 10
    return plus_n

def main():
    N = int(input('Введите число: '))
    if N < 0:
        print('Число не удовлетворяет условию N > 0 \n')
        main()
        return 0
    total_sum = sum_n(N)
    total_amount = amount(N)
    print('Сумма цифр:', total_sum)
    print('Кол-во цифр в числе:', total_amount)
    print('Разность суммы и кол-ва цифр:', round(total_sum / total_amount))

main()