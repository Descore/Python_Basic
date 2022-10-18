# TODO здесь писать код

text = input('Введите строку: ')
text = text[::-1]

h_list = [i for i in range(len(text)) if text[i] == 'h']

if len(h_list) > 2:
    h_list[1] = h_list[len(h_list)-1]

print('Развернутая последовательность между первым и последним h:', text[h_list[0]+1:h_list[1]])
