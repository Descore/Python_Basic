
str_in = 'abcd'
tuple_in = (10, 20, 30, 40)

short_len = min(len(tuple_in), len(str_in))

print('Результат:')
result = ((str_in[i], tuple_in[i]) for i in range(short_len))

print(result)
for i in result:
    print(i)