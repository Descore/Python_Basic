# TODO здесь писать код
import math

def local_reverse(N):
    N_reverse = 0
    while N != 0:
        N_reverse += (N % 10)
        N_reverse *= 10
        N = N // 10
    N_reverse //= 10

    return N_reverse

def reverse(N):
    counter = 0

    whole = int(N)
    whole_reverse = local_reverse(whole)

    residue = N - int(N)
    while (N % 1) != 0:
        N *= 10
        counter += 1
    residue = round(residue, counter)
    residue *= 10 ** counter

    residue_reverse = local_reverse(residue)
    residue_reverse *= 0.1 ** counter

    return whole_reverse + residue_reverse

def main():
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    mir_num_1 = reverse(num_1)
    mir_num_2 = reverse(num_2)
    print('Первое число наоборот: ', mir_num_1)
    print('Второе число наоборот: ', mir_num_2)
    print('Сумма: ', mir_num_1 + mir_num_2)

main()