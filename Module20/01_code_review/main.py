students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def func_students(dict_students):
    string_name = 0

    list_interests = set([dict_students[i]['interests'][j]
                          for i in dict_students
                          for j in range(len(dict_students[i]['interests']))
                          ])

    for i in dict_students:
        string_name += len(dict_students[i]['surname'])

    return list_interests, string_name


pairs = [(i, students[i]['age']) for i in students]
print('Список пар "ID студента — возраст":', pairs)

total_list = func_students(students)
print('Полный список интересов всех студентов:', total_list[0])
print('Общая длина всех фамилий студентов:', total_list[1])

