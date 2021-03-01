# -*- coding: utf-8 -*-

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

import simple_draw as sd

sd.resolution = (600, 600)


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

point_triangle = sd.get_point(100, 100)
sd_regular_polygon(point=point_triangle, angle=0, length=100, sides=3, color=current_color)

point_triangle = sd.get_point(100, 400)
sd_regular_polygon(point=point_triangle, angle=0, length=100, sides=4, color=current_color)

point_triangle = sd.get_point(400, 100)
sd_regular_polygon(point=point_triangle, angle=0, length=100, sides=5, color=current_color)

point_triangle = sd.get_point(400, 400)
sd_regular_polygon(point=point_triangle, angle=0, length=100, sides=6, color=current_color)

sd.pause()

# зачёт! 🚀
