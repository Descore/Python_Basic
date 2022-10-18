text_dict = dict()
inverted_dict = dict()

text_in = input('Введите текст: ')

for i in text_in:
    text_dict.update({i: text_in.count(i)})

print('Оригинальный словарь частот:')
for k, v in text_dict.items():
    print(k, ':', v)

indexes = set(text_dict.values())
for i in indexes:
    words_list = [k for k, v in text_dict.items() if i == v]
    inverted_dict.update({i: words_list})

print('\n Инвертированный словарь частот:')
for k, v in inverted_dict.items():
    print(k, ':', v)


