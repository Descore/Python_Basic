
synonyms_dict = dict()
pairs = []
amount = int(input('Введите количество пар слов: '))

for i in range(amount):
        pairs = (input(str(i+1) + ' пара: ')).split(' - ')
        synonyms_dict.update({pairs[0]: pairs[1]})


def compare():
        word_user = input('Введите слово: ')

        for k, v in synonyms_dict.items():
                if word_user.lower() == k.lower():
                        print('Синоним:', v)
                        break
                elif word_user.lower() == v.lower():
                        print('Синоним:', k)
                        break
        else:
                print('Такого слова в словаре нет.')
                compare()
                return 0


compare()
