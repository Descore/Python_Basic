# TODO здесь писать код
N = int(input('Введите длину списка: '))

nums = [1 if x % 2 == 0 else x % 5 for x in range(N)]
print(nums)