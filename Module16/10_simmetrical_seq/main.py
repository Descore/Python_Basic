# TODO здесь писать код

nums = []
reversed_nums = []
add_nums = []

N = int(input('Кол-во чисел: '))

for _ in range(N):
    nums.append(int(input('Число: ')))

print('Последовательность:', nums)

reversed_nums = nums[::-1]

for i in range(len(nums)):
    if nums[i::] == reversed_nums[:len(reversed_nums) - i:]:
        add_nums.extend(reversed_nums[len(reversed_nums) - i::])
        break

print('Нужно приписать чисел:', len(add_nums))
print('Cами числа:', add_nums)
