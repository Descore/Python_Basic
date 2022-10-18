players_list = {}

notes = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for i in range(notes):
    note = input(str(i+1) + '-я запись: ').split()
    players_list.update({i: {note[1]: note[0]}})

def max_points():
    points = 0
    name = ''
    for i in range(notes):
        for k, v in players_list[i].items():
            if int(v) > points:
                points = int(v)
                name = k

    for i in range(notes):
        for k in players_list[i].keys():
            if k == name:
                players_list.update({i: {name: 0}})

    return name, points


print('Итоги соревнований: ')
for i in range(3):
    place = max_points()
    print(str(i+1) + '-е место:', place[0], place[1])




