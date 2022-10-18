orders_dict = dict()
amount_orders = int(input('Введите количество заказов: '))

for i in range(amount_orders):
    order = input(str(i+1) + ' заказ: ').split()
    if order[0] not in orders_dict:
        orders_dict[order[0]] = {order[1]: int(order[2])}
    else:
        if order[1] not in orders_dict[order[0]]:
            orders_dict[order[0]][order[1]] = int(order[2])
        else:
            orders_dict[order[0]][order[1]] += int(order[2])

for key_fio, value_order in sorted(orders_dict.items()):
    print(key_fio, ':')
    for key_pizza, value_amount in sorted(value_order.items()):
        print('\t', key_pizza, ':', value_amount)
