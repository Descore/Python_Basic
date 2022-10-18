word = input('Введите строку: ').lower()
chars = set()

for i in word:
    if i in chars:
        chars.remove(i)
    else:
        chars.add(i)

if len(chars) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')