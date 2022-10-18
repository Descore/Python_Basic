violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

music_list = []
time = 0

N = int(input('Сколько песен выбрать? '))

for i in range(N):
    music_list.append(input('Название ' + str(i+1) + ' песни: '))

for i in range(len(music_list)):
    for j in range(len(violator_songs)):
        if music_list[i] == violator_songs[j][0]:
            time += violator_songs[j][1]

print('Общее время звучания песен:', round(time, 4))


