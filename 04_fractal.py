# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1200, 600

point_0 = sd.get_point(500, 5)


def branch(point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, length=length, angle=angle)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - 30
    next_length = length * 0.75
    branch(point=next_point, angle=next_angle, length=next_length)
    other_angle = angle + 30
    branch(point=next_point, angle=other_angle, length=next_length)


branch(point=point_0, angle=90, length=130)

# зачёт первой части


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# зачёт! 🚀

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
