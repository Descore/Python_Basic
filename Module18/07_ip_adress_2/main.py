# TODO здесь писать код

IP = input('Введите IP: ')
logic = True

check_ip = IP.split('.')

if len(check_ip) == 4:
    for i in range(4):
        if check_ip[i].isdigit() or (check_ip[i][0] == '-' and check_ip[i][1:].isdigit()):
            if int(check_ip[i]) > 255:
                print(int(check_ip[i]), 'превышает 255')
                logic = False
            elif int(check_ip[i]) < 0:
                print(int(check_ip[i]), 'меньше 0')
                logic = False
        else:
            print(check_ip[i], '- не целое число')
            logic = False
else:
    print('Адрес - это четыре числа, разделенные точками')
    logic = False

if logic:
    print('IP-адрес корректен')

