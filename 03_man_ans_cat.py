# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я кот - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.animal_food -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} теперь будет жить с нами'.format(self.name), color='cyan')

    def sleep(self):
        self.fullness -= 10
        cprint('{} спал целый день'.format(self.name), color='yellow')

    def naughty(self):
        self.house.mood += 5
        self.fullness -= 10
        cprint('{} драл обои'.format(self.name), color='yellow')

    def dead_cat(self):
        cprint('{} кот мёртв!'.format(self.name), color='yellow')
        self.fullness = -50

    def act(self):
        dice = randint(1, 3)
        if self.fullness < 0:
            self.dead_cat()
        elif self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.naughty()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def clean_the_house(self):
        cprint('{} убрался дома'.format(self.name), color='blue')
        self.house.mood -= 100
        if self.house.mood < 0:
            self.house.mood = 0
        self.fullness -= 20

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_for_animal(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.animal_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.animal_food < 20:
            self.shopping_for_animal()
        elif self.house.money < 50:
            self.work()
        elif self.house.mood > 90:
            self.clean_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 100
        self.money = 100
        self.animal_food = 0
        self.mood = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачей еды {}, грязь {}'.format(
            self.food, self.money, self.animal_food, self.mood
        )


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
    Cat(name='Матроскин'),
    Cat(name='Мурзик'),
    Cat(name='Рыська'),
    Cat(name='Ливер')
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# зачёт! 🚀
