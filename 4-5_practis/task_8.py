print('Задача')
#
# Задача 8. Хватит ли зарплаты
#
#
# Что нужно сделать
#
# Георгий работает неофициально по часам, и его зарплата высчитывается по следующей формуле:
#
# Он хочет понять, сколько часов нужно отработать, чтобы хватило на погашение кредита и еду.
#
# Напишите программу, которая запрашивает у пользователя три числа: количество отработанных часов,
# остаток по кредиту и количество денег на еду. После этого рассчитывается зарплата по формуле,
# и если зарплата больше либо равна денежной сумме, которая требуется на кредит и еду, то выводится сообщение:
# «Часов хватает. Можно отдохнуть», в противном случае: «Часов не хватает. Придётся работать!».

# Пример:
#
# Введите отработанные часы: 80
#
# Введите остаток по кредиту: 1000
#
# Введите траты на еду: 5000
#
# Часов не хватает. Придётся работать!

hours = int(input())
kredit = int(input())
eat = int(input())

zp = ((200 * hours) / 2 ** 3) + 3
if zp >= eat + kredit:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')

