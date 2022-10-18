players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
list_i = []
total_list = []

for k, v in players.items():
    for i in range(len(k)):
        list_i.append(k[i])
    for j in range(len(v)):
        list_i.append(v[j])
    total_list.append(tuple(list_i))
    list_i = []

print(total_list)
