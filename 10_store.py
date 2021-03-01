#!/usr/bin/env python
# -*- coding: utf-8 -*-



goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}



store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}




lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_cost = ((store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']) + \
            (store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']))

table_quantity = (store[goods['Стол']][0]['quantity']+store[goods['Стол']][1]['quantity'])

print('Стол -', table_quantity, 'шт, стоимость', round(table_cost, 2), 'руб')

sofa_cost = ((store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']) +
             (store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']))

sofa_quantity = (store[goods['Диван']][0]['quantity']+store[goods['Диван']][1]['quantity'])

print('Диван -', sofa_quantity, 'шт, стоимость', round(sofa_cost, 2), 'руб')


chair_cost = ((store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']) +
             (store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']) +
              (store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']))

chair_quantity = (store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] +
             store[goods['Стул']][2]['quantity'])

print('Стул -', chair_quantity, 'шт, стоимость', round(chair_cost, 2), 'руб')

# зачёт! 🚀


# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.



##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
