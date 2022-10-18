# TODO здесь писать код
text = input('Введите текст: ')

vowels = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я',
          'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

out_vowels = [i_text for i_text in text for i_vowels in vowels if i_text == i_vowels]

print(out_vowels)
