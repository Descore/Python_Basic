# TODO здесь писать код

while True:
    filename = input('Название файла: ')

    if filename.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
        print('Ошибка: название начинается на один из специальных символов \n')

    elif not filename.endswith('.txt' or '.docx'):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx \n')
    else:
        print('Файл назван верно.')
        break

