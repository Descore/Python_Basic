# TODO здесь писать код

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
R = float(input('Введите радиус: '))

if x**2 + y**2 <= R**2:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
