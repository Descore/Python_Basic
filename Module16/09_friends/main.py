# TODO здесь писать код

friends = []

amount_friends = int(input('Кол-во друзей: '))
notes = int(input('Кол-во расписок: '))

for i in range(amount_friends):
    friends.append([i, 0])

def exhange_cash():
    whom = int(input('Кому: '))
    from_to = int(input('От кого: '))
    amount = int(input('Сколько: '))

    friends[whom-1][1] += amount
    friends[from_to-1][1] -= amount

for i in range(notes):
    print('\n', i+1, 'расписка')
    exhange_cash()


print('\nБаланс друзей:')
for i in range(len(friends)):
    print(i+1, ':', friends[i][1])
