# TODO здесь писать код

count = 0
logic_up_symb = False

while True:
    password = input('Придумайте пароль: ')

    if len(password) >= 8:
        for i in password:
            if logic_up_symb == False:
                logic_up_symb = i.isupper()
            if i.isdigit():
                count += 1

    if logic_up_symb and count >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз. \n')