print('Задача')

# Задача 2. Как поступить?
#
# Илья хочет в лучший вуз страны, а для этого нужно не только хорошо сдать экзамены (балл должен быть больше 280), но и иметь золотую медаль.
#
# Напишите программу, которая запрашивает у пользователя два числа: результат экзаменов и наличие золотой медали (0 — нет медали, 1 — медаль есть), а затем проверяет, поступил ли Илья в вуз. Выведите соответствующее сообщение.
#
#
# Пример:
#
# Сколько баллов набрал? 290
#
# Есть медаль? 1
#
# Поздравляем! Ты поступил!
#
#
# Пример 2:
#
# Сколько баллов набрал? 269
#
# Есть медаль? 1
#
# К сожалению, ты не прошёл в наш университет.

score = int(input())
m = int(input())
if score > 280 and m == 1:
    print('ok')
else:
    print('no')
