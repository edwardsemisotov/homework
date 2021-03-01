# -*- coding: utf-8 -*-
import random
import simple_draw as sd

snowflake_list = []


def sd_spawn_snowflake():
    x_point = random.randint(10, sd.resolution[0] - 10)
    snowflake_len = random.randint(10, 40)
    speed = snowflake_len / 5
    return [x_point, sd.resolution[1], snowflake_len, speed]


def spawn_snowflakes(N):
    for i in range(N):
        snowflake_list.append(sd_spawn_snowflake())


def draw_snowflakes_color(color):
    for snowflake in snowflake_list:
        point = sd.get_point(*snowflake[0:2])
        sd.snowflake(center=point, length=snowflake[2], color=color)


def shift_snowflakes():
    for snowflake in snowflake_list:
        snowflake[0] -= random.randint(11, 18) / 10
        snowflake[1] -= snowflake[3]


def numb_reach_down_screen():
    snowflake_down_list = []
    for i in range(len(snowflake_list)):
        snowflake = snowflake_list[i]
        if snowflake[1] < 50:
            snowflake_down_list.append(i)
    return snowflake_down_list


def del_snowflakes(snowflake_del_list):
    for i in sorted(set(snowflake_del_list), reverse=True):
        del snowflake_list[i]
