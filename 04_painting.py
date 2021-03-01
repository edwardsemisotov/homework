# -*- coding: utf-8 -*-
from functions_package import raindow_draw as rd
from functions_package import branch
from functions_package import snowflake as sf
from functions_package import sun
from functions_package import smile
from functions_package import home
import simple_draw as sd
import random

sd.resolution = (1200, 600)

rd.rainbow_draw_kill_me_pls(step=5, width=5, start_point=sd.get_point(1250, 400), end_point=sd.get_point(800, 700))
home.home(left_bot=(400, 0), r_top=(600, 200))
frame_number = 0

snowflake_list = []
N = 50
for i in range(N):
    snowflake_list.append(sf.sd_spawn_snowflake())

while True:
    sd.start_drawing()
    snowflake_del_list = []
    frame_number += 1

    wind_speed = frame_number % 20
    if wind_speed > 10:
        wind_speed = 20 - wind_speed
    wind_speed = wind_speed - 5
    sd.rectangle(left_bottom=sd.get_point(700, 0), right_top=sd.get_point(1200, 300), color=sd.background_color,
                 width=0)
    sd.rectangle(left_bottom=sd.get_point(390, 390), right_top=sd.get_point(910, 600), color=sd.background_color,
                 width=0)
    branch.branch(point=sd.get_point(1000, 5), angle=90, length=70, wind=wind_speed)
    branch.branch(point=sd.get_point(850, 5), angle=90, length=50, wind=wind_speed)

    sun.sun(point=sd.get_point(600, 500), radius=50, current_shift=frame_number * 5)
    smile.smile(x=600, y=500, color=sd.COLOR_BLACK)
    for i in range(len(snowflake_list)):
        snowflake = snowflake_list[i]
        point = sd.get_point(*snowflake[0:2])
        snowflake[0] -= random.randint(11, 18) / 10
        if snowflake[1] > 50:
            snowflake[1] -= snowflake[3]
        else:
            snowflake_del_list.append(i)
        sd.snowflake(center=point, length=snowflake[2], color=sd.background_color)

    for snowflake in snowflake_list:
        point = sd.get_point(*snowflake[0:2])
        sd.snowflake(center=point, length=snowflake[2])

    for i in reversed(snowflake_del_list):
        del snowflake_list[i]
        snowflake_list.append(sf.sd_spawn_snowflake())
    sd.finish_drawing()

    if sd.user_want_exit():
        break
    sd.sleep(0.1)

sd.pause()
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# зачёт! 🚀
