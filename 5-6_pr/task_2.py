print('Задача')
one = int(input())
two = int(input())
three = int(input())

if one > two and one > three:
    print("one", one)
elif two > three:
    print('two', two)
else:
    print('three', three)
