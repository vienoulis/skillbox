print('Задача 6')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

print('Сумма:', str(first_num % 100 + second_num % 100))