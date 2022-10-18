# TODO здесь писать код

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
            'ы', 'ь', 'э', 'ю', 'я']
result = ''

msg = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

cipher = [alphabet[(alphabet.index(w) + shift) % 33] if w != ' ' else ' ' for w in msg]

for i in cipher:
    result += i

print(result)
