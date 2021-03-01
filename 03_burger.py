# -*- coding: utf-8 -*-
import my_burger as mb


import pprint

my_burger_list = []


def choose_ingredients_burger(my_burger_list):
    ingredients = (
        ('майонез', mb.mayonnaise),
        ('сыр', mb.cheese),
        ('помидор', mb.tomato),
        ('огурец', mb.cucumber),
        ('кoтлета', mb.cutlets),
        ('булочка', mb.buns),
        ('хочу забрать свой бургер',)
    )
    print('Выберите ингредиенты из списка')
    for i in range(len(ingredients)):
        print(i + 1, ingredients[i][0])
    while True:

        ingredients_number = int(input('Введите номер ингредиента по одному: '))

        if ingredients_number < 1 or ingredients_number > len(ingredients):
            return print('нет такого ингредиента, начните заново')
        if ingredients_number >= 1 and ingredients_number < len(ingredients):
            ingredients[ingredients_number - 1][1](my_burger_list)
        if ingredients_number == len(ingredients):
            return pprint.pprint('Ваш бургер готов из: ' + ', '.join(my_burger_list))


choose_ingredients_burger(my_burger_list)

# my_burger_list.append(*mb.buns())
# my_burger_list.append(*mb.cutlets())
# my_burger_list.append(*mb.tomato())
# my_burger_list.append(*mb.mayonnaise())
# my_burger_list.append(*mb.cheese())
# pprint.pprint('Ваш бургер состоит из: ' + ', '.join(my_burger_list))


# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# зачёт! 🚀
