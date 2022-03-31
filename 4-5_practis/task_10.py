print('Задача')

# Задача 10. Максимальное число (по желанию)
#
#
# Что нужно сделать
#
# Пользователь вводит три числа.
#
# Напишите программу, которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Используйте дополнительные переменные, если нужно.

first = int(input())
second = int(input())
third = int(input())

if first > second:
    if first > third:
        print('first', first)
    else:
        print('third', third)
elif second > third:
    print('second', second)
else:
    print('third', third)
