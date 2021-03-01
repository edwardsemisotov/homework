# -*- coding: utf-8 -*-
from district.central_street.house1.room1 import folks as central_h1_r1
from district.central_street.house1.room2 import folks as central_h1_r2
from district.central_street.house2.room1 import folks as central_h2_r1
from district.central_street.house2.room2 import folks as central_h2_r2
from district.soviet_street.house1.room1 import folks as soviet_h1_r1
from district.soviet_street.house1.room2 import folks as soviet_h1_r2
from district.soviet_street.house2.room1 import folks as soviet_h2_r1
from district.soviet_street.house2.room2 import folks as soviet_h2_r2


import pprint

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

district_list = [*central_h1_r1, *central_h1_r2, *central_h2_r1, *central_h2_r2, *soviet_h1_r1, *soviet_h1_r2,
                 *soviet_h2_r1,
                 *soviet_h2_r2]

pprint.pprint('На районе живут: ' + ', '.join(district_list))

# зачёт! 🚀
