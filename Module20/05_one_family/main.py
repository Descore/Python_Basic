families = {
    ("Иванов", "Иван"): 40,
    ("Иванова", "Татьяна"): 35,
    ("Петров", "Петя"): 12,
    ("Петров", "Степан"): 30,
    ("Петрова", "Анастасия"): 28
}

choose = input('Введите фамилию: ').lower()

for k, v in families.items():
    if (k[0].lower() == choose) or (k[0].lower() == choose+'а'):
        print(k[0], k[1], v)