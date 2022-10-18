max_num = int(input('Введите максимальное число: '))
nums = {x for x in range(1, max_num + 1)}

while True:
    nums_in = (input('Нужное число есть среди вот этих чисел: '))
    if nums_in == 'Помогите!':
        break
    nums_list = {int(x) for x in nums_in.split()}
    answer = input('Ответ Артёма: ')
    if answer.lower() == 'да':
        nums &= nums_list
    else:
        nums -= nums_list
    print(nums)



