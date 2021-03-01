# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

def draw_bubble(point, step, radius, color=sd.COLOR_BLACK):
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2, color=color)
        radius += step


point = sd.get_point(350, 350)
draw_bubble(point=point, step=5, radius=5, color=sd.COLOR_YELLOW)
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 500)

    draw_bubble(point=point, radius=10, step=5, color=sd.COLOR_DARK_ORANGE)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        draw_bubble(point=point, radius=5, step=5, color=sd.COLOR_DARK_PURPLE)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 5)

    draw_bubble(point=point, radius=20, step=step, color=sd.random_color())

sd.pause()

# зачёт! 🚀
