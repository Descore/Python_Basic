# TODO здесь писать код

usr_str = input('Введите строку: ')
result = ''
count = 0

for i in range(1, len(usr_str)):
    if usr_str[i] == usr_str[i-1]:
        count += 1
    else:
        result += usr_str[i-1] + str(count+1)
        count = 0
result += usr_str[i] + str(count+1)

print(result)