# TODO здесь писать код

countries_dict = dict()
countries_list = []

amount = int(input('Введите количество стран: '))
logic = True

for i in range(amount):
    countries = input(str(i+1) + ' страна: ')
    countries_list = countries.split()
    countries_dict[countries_list[0]] = countries_list[1:]

for j in range(3):
    print()
    city_in = input(str(j+1) + ' город: ')
    for country, city in countries_dict.items():
        if city.count(city_in) >= 1:
            print('Город', city_in, 'расположен в стране', country)
            logic = False
            break
        logic = True
    if logic:
        print('По городу', city_in, 'нет данных')
