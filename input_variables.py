import pygame as pg


def input_variables():
    flag = True
    while flag:
        try:
            size = tuple(map(int, input('Введите размеры окна (ширину и высоту через пробел): ').split()))
            if len(size) == 2:
                flag = False
            else:
                print('Вы ошиблись, попробуйте снова')
        except ValueError:
            print('Вы ошиблись, попробуйте снова')
    flag = True
    while flag:
        try:
            n = int(input('Введите количество шайб: '))
            if n > 0:
                flag = False
            elif n == 0:
                return None, size
            else:
                print('Число меньше 1, попробуйте снова')
        except ValueError:
            print('Вы ошиблись попробуйте снова')
    objects = []
    for i in range(n):
        flag = True
        while flag:
            try:
                x = float(input('Введите x координату центра ' + str(i+1) + ' шайбы: '))
                flag = False
            except ValueError:
                print('Вы ошиблись попробуйте снова')

        flag = True
        while flag:
            try:
                y = float(input('Введите y координату ' + str(i+1) + ' центра шайбы: '))
                flag = False
            except ValueError:
                print('Вы ошиблись попробуйте снова')

        flag = True
        while flag:
            try:
                r = float(input('Введите радиус ' + str(i+1) + ' шайбы: '))
                flag = False
            except ValueError:
                print('Вы ошиблись попробуйте снова')

        flag = True
        while flag:
            try:
                m = float(input('Введите массу ' + str(i+1) + ' шайбы: '))
                flag = False
            except ValueError:
                print('Вы ошиблись попробуйте снова')

        flag = True
        while flag:
            try:
                vx = float(input('Введите x составляющую скорости ' + str(i+1) + ' шайбы: '))
                flag = False
            except ValueError:
                print('Вы ошиблись попробуйте снова')

        flag = True
        while flag:
            try:
                vy = float(input('Введите y составляющую скорости ' + str(i+1) + ' шайбы: '))
                flag = False
            except ValueError:
                print('Вы ошиблись попробуйте снова')
        color = input('Введите цвет шайбы в HEX формате: ')
        color = hex_to_rgb(color)

        objects.append([r, m, vx, vy, x, y, pg.Color(color)])
    return objects, size


def hex_to_rgb(HEX):
    r = int(HEX[0] + HEX[1], 16)
    g = int(HEX[2] + HEX[3], 16)
    b = int(HEX[4] + HEX[5], 16)
    return (r, g, b)