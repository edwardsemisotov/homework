# -*- coding: utf-8 -*-

import random
import simple_draw as sd

sd.resolution = 1700, 900


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:
    def __init__(self, speed, length, x, y):
        self.x = x
        self.y = y
        self.speed = speed
        self.length = length

    def update(self, wind):
        self.x += wind * self.speed
        self.y -= self.speed

    def draw(self):
        self.draw_internal(color=sd.COLOR_WHITE)

    def clear_previous_picture(self):
        self.draw_internal(color=sd.background_color)

    def draw_internal(self, color):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=color)

    def can_fall(self):
        return self.y > self.length


def get_flakes(count):
    result = []
    for i in range(count):
        flake_length = random.randint(20, 80)
        result.append(Snowflake(x=random.randint(10, sd.resolution[0]), y=sd.resolution[1], length=flake_length,
                                speed=flake_length / 5))
    return result


def get_fallen_flakes(snowflake_list):
    result = 0
    for i in range(len(snowflake_list) - 1, -1, -1):
        if not snowflake_list[i].can_fall():
            del snowflake_list[i]
            result += 1
    return result


def append_flakes(snowflake_list, count):
    snowflake_list.extend(get_flakes(count))


def get_wind_power():
    half_res = sd.resolution[0] / 2
    mouse_pos = sd.get_mouse_state()[0]
    return (mouse_pos.x - half_res) / half_res


N = 50
flakes = get_flakes(count=N)
while True:
    wind_power = get_wind_power()
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.update(wind_power)
        flake.draw()
    sd.finish_drawing()
    fallen_flakes = get_fallen_flakes(flakes)
    if fallen_flakes:
        append_flakes(flakes, count=fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()

# зачёт! 🚀
