print('Задача 3. Следующее и предыдущее')

# В олимпиаде по программированию участвовали 1000 человек,
# и программа автоматически распределила их по количеству баллов.
# Иногда количество баллов у участников одинаковое,
# и тогда комиссии нужно посмотреть фамилии одного из таких участников,
# а также его соседей, это реализует специальная часть алгоритма.
#
# Напишите программу,
# которая получает от пользователя число и выводит на экран два ответа — следующее и предыдущее число.
# Результат:

# Введите число: 5
# После числа 5 идет число 6
# До числа 5 идет число 4
number = int(input('Введите число: '))
number += 1
print("Следущее число:", number)
number -= 2
print("Предыдущее число:", number)
