# -*- coding: utf-8 -*-
import simple_draw as sd

def smile(x, y, color, radius):

    offset_lips = (30, 10)
    offset_eye = (20, 10)

    point_center = sd.get_point(x, y)
    sd.circle(center_position=point_center, radius=radius, color=color, width=5)
    point_left_eye = sd.get_point(point_center.x - offset_eye[0], point_center.y + offset_eye[1])
    sd.circle(center_position=point_left_eye, radius=5, color=color)
    point_right_eye = sd.get_point(point_center.x + offset_eye[0], point_center.y + offset_eye[1])
    sd.circle(center_position=point_right_eye, radius=5, color=color)

    point1 = sd.get_point(point_center.x - offset_lips[0], point_center.y)
    point2 = sd.get_point(point_center.x - offset_lips[1], point_center.y - offset_lips[1])
    point3 = sd.get_point(point_center.x + offset_lips[1], point_center.y - offset_lips[1])
    point4 = sd.get_point(point_center.x + offset_lips[0], point_center.y)
    smile_point_list = [point1, point2, point3, point4]
    sd.lines(point_list=smile_point_list, color=color, closed=False, width=3)


for _ in range(10):
    smile_param = sd.random_point()
    smile(smile_param.x, smile_param.y, sd.COLOR_RED)

sd.pause()

# зачёт! 🚀


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
