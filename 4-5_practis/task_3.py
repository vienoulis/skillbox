print('Задача 3. Следим за зубами')

# Задача 3. Следим за зубами
#
# Что нужно сделать
#
# Стоматолог посоветовал Маше использовать зубную нить каждый чётный день. Чтобы не забывать,
# Маша написала скрипт на Python, который в случае чего напоминает ей о совете стоматолога.
#
# Напишите программу, которая проверяет, чётное ли число ввёл пользователь, и выводит соответствующее сообщение.
#
# Подсказка: для проверки чётности используйте оператор %.
#

number_of_day = int(input('Введите номер дня: '))
if number_of_day % 2 == 0:
    print('Не забудь почистить зубы нитью')

