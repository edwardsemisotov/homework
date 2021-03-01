# -*- coding: utf-8 -*-
import simple_draw as sd
import random

sd.resolution = 1200, 600

N = 50
y_point = 500
snowflake_list = []


def sd_spawn_snowflake():
    x_point = random.randint(10, sd.resolution[0] - 10)
    snowflake_len = random.randint(10, 40)
    speed = snowflake_len / 5
    return [x_point, y_point, snowflake_len, speed]


for i in range(N):
    snowflake_list.append(sd_spawn_snowflake())

while True:
    sd.start_drawing()
    snowflake_del_list = []

    for i in range(len(snowflake_list)):
        snowflake = snowflake_list[i]
        point = sd.get_point(*snowflake[0:2])
        snowflake[0] -= random.randint(11, 18)/10
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
        snowflake_list.append(sd_spawn_snowflake())
    sd.finish_drawing()

    if sd.user_want_exit():
        break
    sd.sleep(0.1)

sd.pause()

# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# зачёт! 🚀
