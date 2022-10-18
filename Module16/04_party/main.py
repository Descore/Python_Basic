guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    action = str(input('Гость пришел или ушел? '))
    if action == 'пришел':
        name = str(input('Имя гостя: '))
        if len(guests) < 6:
            print('Привет,', name)
            guests.append(name)
        else:
            print('Прости,', name, ',но мест нет.')

    elif action == 'ушел':
        name = str(input('Имя гостя: '))
        print('Пока,', name)
        guests.remove(name)

    elif action == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break