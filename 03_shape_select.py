# -*- coding: utf-8 -*-

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

import simple_draw as sd

sd.resolution = (600, 600)


def choose_figure():
    figure = (
        ('треугольник', 3),
        ('квадрат', 4),
        ('пятиугольник', 5),
        ('шестиугольник', 6),
    )
    print('Выберите фигуру из списка')
    for i in range(len(figure)):
        print(i + 1, figure[i][0])
    figure_number = int(input('Введите номер фигуры, которую нужно нарисовать: '))

    if figure_number < 1 or figure_number > len(figure):
        print('нет такой фигуры , будет Треугольник!')
        figure_number = 1
    figure_number -= 1
    return figure[figure_number][1]


def choose_color():
    colors = (
        ('красный', sd.COLOR_RED),
        ('оранжевый', sd.COLOR_ORANGE),
        ('желтый', sd.COLOR_YELLOW),
        ('зелёный', sd.COLOR_GREEN),
        ('синий', sd.COLOR_BLUE),
        ('пурпурный', sd.COLOR_PURPLE),
        ('голубой', sd.COLOR_CYAN),
    )

    print('Выберите цвет из списка')
    for i in range(len(colors)):
        print(i + 1, colors[i][0])
    color_number = int(input('Введите номер цвета, которым нужно нарисовать фигуры: '))

    if color_number < 1 or color_number > len(colors):
        print('нет такого цвета, буду калякать КРОВЬЮ')
        color_number = 1
    color_number -= 1
    return colors[color_number][1]


def sd_regular_polygon(point, angle, length, sides, color=sd.COLOR_RED):
    current_start = point
    current_angle = angle
    angle_step = 360 / sides
    for i in range(sides - 1):
        v = sd.get_vector(start_point=current_start, angle=current_angle, length=length)
        v.draw(color=color)
        current_start = v.end_point
        current_angle += angle_step
    sd.line(start_point=current_start, end_point=point, color=color)


current_color = choose_color()

point_triangle = sd.get_point(300, 300)
sd_regular_polygon(point=point_triangle, angle=0, length=100, sides=choose_figure(), color=current_color)

sd.pause()

# зачёт! 🚀
