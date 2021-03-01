# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

month = 0
educational_grant_sum = 0
expenses_sum = 0

exp = expenses

while month < 10:
    expenses_sum += exp
    exp += exp * 0.03
    educational_grant_sum += educational_grant
    month += 1
    # есть такой оператор += сложение с присвоением называется

give_me_money = expenses_sum - educational_grant_sum
print('Студенту надо попросить', round(give_me_money, 2), 'рублей')

# зачёт! 🚀
