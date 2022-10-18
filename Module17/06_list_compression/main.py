# TODO здесь писать код
import random

N = int(input('Кол-во чисел в списке: '))

nums = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия:', nums)

for _ in range(nums.count(0)):
    nums.remove(0)

print('Список после сжатия:', nums)