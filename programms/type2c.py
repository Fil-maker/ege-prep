# В этом подтипе нужно смотреть не на делители чисел, а на их остатки от деления на K (3 в этом случае)

with open('../files/type2c.txt') as file:
    max1, max2, max3a, max3b = 0, 0, 0, 0
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        num = int(text[i])
        if num % 3 == 1 and num > max1:
            max1 = num
        elif num % 3 == 2 and num > max2:
            max2 = num
        elif num % 3 == 0:
            if num > max3a:
                max3a = num
            if num == max3a:
                max3b = num
if (max1 and max2) or (max3b and max3a):
    if max1 + max2 > max3a + max3b:
        print(max1 + max2)
    else:
        print(max3a + max3b)
else:
    print(1)
