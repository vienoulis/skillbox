print('Задача')

# Задача 1. Покупка велосипеда
#
# Напишите программу, которую мы разбирали в рамках теории. Нашему ребёнку нужен новый хороший велосипед.
# Правда, никто из нас в них не разбирается, всё что нам нужно — чтобы велосипед не был устаревшим и
# чтоб скоростей на нём было побольше, а сколько он стоит — пока неважно. Чтобы не искать велосипед на сайте вручную,
# мы хотим написать программу, которая будет проверять каждый велосипед на нужный нам год выпуска и на количество скоростей.
#
# Используя один из логических операторов (and, or), напишите программу из урока,
# которая запрашивает год выпуска велосипеда и количество скоростей на нём и выводит на экран сообщение о том,
# подходит этот велик или нет. Год выпуска — не старше 2018-го, количество скоростей — не менее 24.

ear = int(input())
gear = int(input())

if 2018 < ear and 24 > gear:
    print('no')
else:
    print('yes')
