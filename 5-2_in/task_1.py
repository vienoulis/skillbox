print('Задача 1. Координаты')
#
# Задача 1. Координаты
#
# Мы тестируем 2D-игру, где нужно управлять подводной лодкой.
# У лодки есть координаты в пространстве — X (икс) и Y (игрек). X — это движение вперёд-назад, а Y —  вверх-вниз.
# Соответственно, во время движения лодки меняются и её координаты.
# Во время тестирования игры нам необходимо сравнивать эти координаты и выводить на экран нужное сообщение, в том числе если они равны.
#
#
# Вводятся две координаты — X и Y. С помощью трёх последовательных проверок сравните обе координаты и выведите соответствующее сообщение.
#
#
# Пример:
#
# Введите икс: 5
#
# Введите игрек: 6
#
# X меньше Y
#
#
# Пример 2:
#
# Введите икс: 3
#
# Введите игрек: 3
#
# X равен Y
#
x = int(input())
y = int(input())

if x == y:
    print("Ravny")
if x > y:
    print('x > y')
if x < y:
    print('x < y')