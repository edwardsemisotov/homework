# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (600, 600)

brick_height = 50
y_range = int(sd.resolution[0] / brick_height)
brick_width = 100
x_range = int(sd.resolution[1] / brick_width)

lb_x = 0
lb_y = 0

rt_x = 100
rt_y = 50

for a in range(y_range):

    x = lb_x
    x1 = rt_x
    if a % 2 == 1:
        x = x - brick_width / 2
        x1 = x1 - brick_width / 2
    for _ in range(x_range):
        sd.rectangle(left_bottom=sd.get_point(x, lb_y), right_top=sd.get_point(x1, rt_y), color=sd.COLOR_YELLOW,
                     width=5)
        x += 100
        x1 += 100

    rt_y += 50
    lb_y += 50
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()

# зачёт! 🚀
