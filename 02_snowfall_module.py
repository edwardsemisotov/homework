# -*- coding: utf-8 -*-
import simple_draw as sd
import snowfall

sd.resolution = 1200, 600
N = 50

snowfall.spawn_snowflakes(N)

while True:
    sd.start_drawing()
    snowfall.draw_snowflakes_color(color=sd.background_color)
    snowfall.shift_snowflakes()
    snowfall.draw_snowflakes_color(color=sd.COLOR_WHITE)
    del_list = snowfall.numb_reach_down_screen()
    if del_list:
        snowfall.del_snowflakes(del_list)
        snowfall.spawn_snowflakes(len(del_list))

    sd.finish_drawing()

    if sd.user_want_exit():
        break
    sd.sleep(0.1)

sd.pause()

# Зачёт!
