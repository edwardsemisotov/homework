# -*- coding: utf-8 -*-
import random

_holder = []


def pick_number():
    global _holder
    holder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mix_holder = []
    random.shuffle(holder)
    mix_holder.append(holder[0])
    del holder[0]
    holder.append(0)
    random.shuffle(holder)
    mix_holder.extend(holder[0:3])
    _holder = mix_holder
    print(_holder)  # NOTE для целей отладки и проверки


def bulls_and_cows(number):
    bulls = 0
    cows = 0
    for i in range(len(number)):
        if int(number[i]) == int(_holder[i]):
            bulls += 1
        elif int(number[i]) in _holder:
            cows += 1

    return {'bulls': bulls, 'cows': cows}
