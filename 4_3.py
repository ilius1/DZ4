a=float(input('Введите количество метров '))
d=int(input('Введите 1 для перевода в мили, введите 2 для перевода в дюймы, введите 3 для перевода в ярды '))
if d == 1:
    print('В милях ',a/1067)
elif d == 2:
    print('В дюймах',a/0.0254)
elif d == 3:
    print('В ярдах ',a/0.91)
else:
    print('Вы ввели неверное значение ')
input()