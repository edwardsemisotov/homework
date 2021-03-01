# -*- coding: utf-8 -*-

import simple_draw as sd
# (цикл for)


sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def rainbow_draw(step, width, start_point, end_point):
    for rainbow_line in range(7):
        offset = step * rainbow_line
        current_start = sd.get_point(start_point.x + offset, start_point.y)
        current_end = sd.get_point(end_point.x + offset, end_point.y)
        sd.line(current_start, current_end, color=rainbow_colors[rainbow_line], width=width)


rainbow_draw(step=5, width=4, start_point=sd.get_point(50, 50), end_point=sd.get_point(350, 450))


def vector_length(v):
    return (v[0] * v[0] + v[1] * v[1]) ** 0.5


def vector_multiply(v, n):
    return v[0] * n, v[1] * n


def vector_normalize(v):
    vector_l = vector_length(v)
    if vector_l == 0:
        return (0, 1)
    normal_vector = vector_multiply(v, (1 / vector_l))
    return normal_vector


def rainbow_draw_kill_me_pls(step, width, start_point, end_point):
    vector = ((end_point.x - start_point.x), (end_point.y - start_point.y))
    vector90 = (-vector[1], vector[0])
    normal_vector = vector_normalize(vector90)
    step_vector = vector_multiply(normal_vector, step)

    for rainbow_line in range(7):
        offset_vector = vector_multiply(step_vector, rainbow_line)
        current_start = sd.get_point(start_point.x + offset_vector[0], start_point.y + offset_vector[1])
        current_end = sd.get_point(end_point.x + offset_vector[0], end_point.y + offset_vector[1])
        sd.line(current_start, current_end, color=rainbow_colors[rainbow_line], width=width)


rainbow_draw_kill_me_pls(step=5, width=5, start_point=sd.get_point(450, 450), end_point=sd.get_point(550, 450))

# зачёт! 🚀

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


sd.pause()
