# TODO здесь писать код

def main():
    N = int(input('Введите число: '))
    if N <= 1:
        print('Введено неверное значение \n')
        main()
        return 0

    for i in range(2,N+1):
        if N % i == 0:
            print('Наименьший делитель, отличный от единицы:', i)
            break

main()