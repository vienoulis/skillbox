print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.
number = int(input('Введите четырех значное число: '))
thousands = number % 1000
hundred = thousands % 100
tenths = hundred % 10

print(str(tenths) + str(hundred // 10) + str(thousands // 100) + str(number // 1000))
