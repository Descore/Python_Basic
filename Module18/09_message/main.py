# TODO здесь писать код

msg = input('Сообщение: ')

msg_reverse = msg.split()
simple_words = [x for x in range(len(msg_reverse))]
total_word, word = '', ''

for i in range(len(msg_reverse)):
    if msg_reverse[i].isalpha():
        msg_reverse[i] = msg_reverse[i][::-1]
        simple_words.remove(i)

for j in simple_words:
    for i in msg_reverse[j]:
        if i.isdigit() or i.isalpha():
            word += i
        else:
            total_word += word[::-1]+i
            word = ''

    total_word += word[::-1]
    msg_reverse[j] = total_word
    total_word, word = '', ''

msg_reverse = ' '.join(msg_reverse)

print('Новое сообщение:', msg_reverse)

