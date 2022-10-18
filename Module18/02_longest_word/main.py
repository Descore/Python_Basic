# TODO здесь писать код

max_word = ''

usr_str = input('Введите строку: ')

usr_str = usr_str.split()

for i in usr_str:
    if len(i) > len(max_word):
        max_word = i
print(max_word)
