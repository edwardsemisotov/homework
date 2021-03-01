# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint
import family_params as fp


class House:

    def __init__(self):
        self.food = fp.start_food
        self.money = fp.start_money
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме еды осталось {}, еды для кота осталось {}, денег осталось {}, грязь {}'.format(
            self.food, self.cat_food, self.money, self.dirt
        )

    def dirty_house(self):
        self.dirt += 5


class Being:

    def __init__(self, name, fullness, hunger, alive):
        self.__name = name
        self.__fullness = fullness
        self.__hunger = hunger
        self.__alive = alive
        self.__death_reason = None

    def __str__(self):
        if self.__alive:
            return 'Я - {}, сытость {}'.format(
                self.__name, self.__fullness
            )
        return 'Я - {}, {}'.format(self.__name, self.__death_reason)

    def get_name(self):
        return self.__name

    def is_alive(self):
        return self.__alive

    def __starve(self):
        if not self.__alive:
            print('попытались убить мёртвого')  # проверка на баг
            return
        self.__fullness -= self.__hunger
        if self.__fullness < 0:
            self.die('умер от голода')

    def die(self, reason):
        if not self.__alive:
            return
        self.__alive = False
        self.__death_reason = reason

    def days_till_death_from_starvation(self):
        return self.__fullness / self.__hunger

    def consume_food(self, food_points):
        if not self.__alive:
            print('пытался накормить труп')  # проверка бага
            return
        self.__fullness += food_points

    def act(self):
        if self.__alive:
            self.__starve()


class DomesticBeing(Being):
    def __init__(self, name, fullness, hunger, alive, house):
        super().__init__(name=name, fullness=fullness, hunger=hunger, alive=alive)
        self.house = house


class Human(DomesticBeing):

    def __init__(self, name, fullness, happiness, house):
        super().__init__(name=name, fullness=fullness, alive=True, hunger=10, house=house)
        self.happiness = happiness

    def __str__(self):
        return '{}, счастье {}'.format(
            super().__str__(), self.get_happiness()
        )

    def get_happiness(self):
        return self.happiness

    def sleep(self):
        cprint('{} спал целый день'.format(self.get_name()), color='yellow')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.get_name()), color='yellow')
            self.consume_food(30)  # family_params
            self.house.food -= 10  # family_params
            return True
        else:
            cprint('{} нет еды'.format(self.get_name()), color='red')
            return False

    def act(self):
        super().act()
        if not self.is_alive():
            return
        if self.house.dirt > 90:
            self.happiness -= 10  # family_params
        if self.get_happiness() < 0:
            self.die('умер от депрессии')


class Adult(Human):

    def __init__(self, name, house):
        super().__init__(name=name, fullness=50, happiness=100, house=house)
        self.quantity_money_made = 100  # family_params
        self.quantity_purchased_coat = 0
        self.quantity_purchased_eat = home.food
        self.wage = 300  # family_params

    def work(self):
        cprint('{} сходил на работу'.format(self.get_name()), color='blue')
        self.house.money += self.wage
        self.quantity_money_made += self.wage

    def gaming(self):
        cprint('{} играл в Танки целый день'.format(self.get_name()), color='green')
        self.happiness += 20  # family_params

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.get_name()), color='magenta')
            self.house.money -= 50
            self.house.food += 50
            self.quantity_purchased_eat += 50
        else:
            cprint('{} деньги кончились!'.format(self.get_name()), color='red')

    def shopping_cat_food(self):
        if self.house.money >= 40:
            cprint('{} сходила за кошачей едой в магазин'.format(self.get_name()), color='magenta')
            self.house.money -= 40
            self.house.cat_food += 40
        else:
            cprint('{} деньги кончились!'.format(self.get_name()), color='red')

    def pet_the_cat(self):
        cprint('{} гладил кота'.format(self.get_name()), color='magenta')
        self.happiness += 5

    def buy_fur_coat(self):
        if self.house.money >= 400:
            cprint('{} сходила в магазин и купила шубу'.format(self.get_name()), color='magenta')
            self.house.money -= 350
            self.happiness += 60
            self.quantity_purchased_coat += 1
        else:
            cprint('{} мой муж очень слабо работает, я даже не могу себе купить шубу!'.format(self.get_name()),
                   color='red')

    def clean_house(self):
        cprint('{} убралась дома'.format(self.get_name()), color='blue')
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0


class Husband(Adult):

    def act(self):
        super().act()
        if not self.is_alive():
            return
        dice = randint(1, 4)
        tried_to_eat = False
        if self.days_till_death_from_starvation() < 2:
            tried_to_eat = True
            if self.eat():
                return
        if self.house.money < 250:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2 and tried_to_eat == False:
            self.eat()
        else:
            self.gaming()


class Wife(Adult):

    def act(self):
        super().act()
        if not self.is_alive():
            return
        dice = randint(1, 5)
        if self.days_till_death_from_starvation() < 2:
            if self.eat():
                return
        if self.house.food < 30:
            self.shopping()
        elif self.house.cat_food < 40:
            self.shopping_cat_food()
        elif home.dirt >= 70:
            self.clean_house()
        elif dice == 1:
            self.buy_fur_coat()
        elif dice == 2:
            self.pet_the_cat()
        elif dice == 3:
            self.eat()
        elif dice == 4 and self.house.cat_food < 30:

            self.shopping_cat_food()
        else:
            self.clean_house()


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, fullness=50, happiness=100, house=house)

    def get_happiness(self):
        return 100

    def act(self):
        super().act()
        if not self.is_alive():
            return
        if self.days_till_death_from_starvation() < 2:
            if self.eat():
                return
        self.sleep()


class Cat(DomesticBeing):

    def __init__(self, name, house):
        super().__init__(name, fullness=30, hunger=10, alive=True, house=house)

    def eat(self):
        if self.house.cat_food >= 20:
            cprint('{} поел'.format(self.get_name()), color='yellow')
            self.consume_food(20)
            self.house.cat_food -= 20
            return True
        else:
            cprint('{} нет еды'.format(self.get_name()), color='red')
            return False

    def sleep(self):
        cprint('{} спал целый день'.format(self.get_name()), color='yellow')

    def tear_wallpaper(self):
        self.house.dirt += 5
        cprint('{} драл обои'.format(self.get_name()), color='yellow')

    def act(self):
        super().act()
        if not self.is_alive():
            return
        tried_to_eat = False
        if self.days_till_death_from_starvation() < 2:
            if self.eat():
                return
            tried_to_eat = True
        dice = randint(1, 4)
        if dice == 1 and not tried_to_eat:
            self.eat()
        elif dice == 2:
            self.tear_wallpaper()
        else:
            self.sleep()


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
little_cat = Cat(name='Мурзик', house=home)
little_cat_2 = Cat(name='Блохастик', house=home)
sara = Child(name='Сара', house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirty_house()
    little_cat.act()
    little_cat_2.act()
    serge.act()
    masha.act()
    sara.act()
    cprint(little_cat, color='cyan')
    cprint(little_cat_2, color='cyan')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(sara, color='cyan')
    cprint(home, color='cyan')

cprint('всего денег заработано {}'.format(serge.quantity_money_made), color='cyan')
cprint('всего шуб куплено {}'.format(masha.quantity_purchased_coat), color='cyan')
cprint('всего еды съедено {}'.format(masha.quantity_purchased_eat - home.food), color='cyan')

# зачёт второй части

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

'''
home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
'''

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
