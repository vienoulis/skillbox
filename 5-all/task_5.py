print('Задача')
summ = int(input())

while summ < 10_000:
    x = int(input())
    if x == 3:
        print('вы проиграли все')
        summ = 0
        break
    summ += 500
print(summ)
