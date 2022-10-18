# TODO здесь писать код

size_skates = []
size_foot = []
count = 0

N = int(input('Кол-во коньков: '))
for i in range(N):
    size_skates.append(input('Рзамер ' + str(i+1) + ' пары: '))

K = int(input('\nКол-во людей: '))
for i in range(K):
    size_foot.append(input('Рзамер ноги ' + str(i+1) + ' человека: '))

size_skates.sort()  # чтобы не взять конек слишком большого размера, когда он нужен другому

for i_foot in size_foot:
    for i_skates in size_skates:
        if i_skates >= i_foot:
            size_skates.pop(size_skates.index(i_skates))
            count += 1
            break

print('\n Наибольшее кол-во людей, которые могут взять ролики:', count)

