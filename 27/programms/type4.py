# Ищем максимальное произведение делящееся на 7, но не на 49
with open('../files/type4.txt') as file:
    max7, maxs = 0, 1
    m = 0
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        num = int(text[i])
        if num % 49 != 0 and num % 7 == 0 and max7 < num:
            max7 = num
        if num % 7 != 0 and maxs < num:
            maxs = num

if max7:
    print(max7 * maxs)
else:
    print(1)
