# -*- coding: utf-8 -*-


# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class BaseElement:
    next_el_id = 0
    transformation_rules = {}

    def __init__(self):
        this_el = type(self)
        self.register_element(this_el)

    def add_transformation(self, el_1, el_2, result):
        if el_1 not in BaseElement.transformation_rules:
            BaseElement.transformation_rules[el_1] = {}
        BaseElement.transformation_rules[el_1][el_2] = result

    def register_element(self, this_el):
        if 'el_id' in dir(this_el):
            return
        this_el.el_id = BaseElement.next_el_id
        BaseElement.next_el_id += 1
        self.add_transformation(this_el.el_id, this_el.el_id, this_el)
        if 'get_transformations' in dir(this_el):
            for key, value in this_el().get_transformations().items():
                self.register_element(key)
                self.add_transformation(key.el_id, this_el.el_id, value)
                self.add_transformation(this_el.el_id, key.el_id, value)

    def __str__(self):
        return self.el_name

    def __add__(self, other):
        self_rules = BaseElement.transformation_rules[self.el_id]
        if other.el_id not in self_rules:
            return None
        return self_rules[other.el_id]()


class Water(BaseElement):
    el_name = 'вода'

    def get_transformations(self):
        return {Air: Storm,
                Fire: Steam,
                Earth: Mud}


class Air(BaseElement):
    el_name = 'воздух'

    def get_transformations(self):
        return {Fire: Lightning,
                Earth: Dust}


class Fire(BaseElement):
    el_name = 'огонь'

    def get_transformations(self):
        return {Earth: Lava}


class Earth(BaseElement):
    el_name = 'земля'


class Storm(BaseElement):
    el_name = 'шторм'


class Steam(BaseElement):
    el_name = 'пар'


class Mud(BaseElement):
    el_name = 'грязь'


class Lightning(BaseElement):
    el_name = 'молния'


class Dust(BaseElement):
    el_name = 'пыль'


class Lava(BaseElement):
    el_name = 'лава'


print(Air() + Fire())
print(Earth() + Water())
print(Water() + Water())
print(Water() + Storm())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# зачёт! 🚀
