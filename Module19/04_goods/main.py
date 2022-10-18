goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

total_quantity, total_price = 0, 0

for k, v in goods.items():
    for k2, v2 in store.items():
        if v == k2:
            for q in range(len(store[k2])):
                total_price += store[k2][q]['quantity'] * store[k2][q]['price']
                total_quantity += store[k2][q]['quantity']

            print(k, '-', total_quantity, 'шт.,', 'стоимость', total_price, 'руб.')
            total_price, total_quantity = 0, 0