# Идея здесь в том, чтобы отловить делители R, которые помогут найти наибольшие числа, удовлетворяющие условию
# Здесь ищем наибольшее произведение чисел, делящееся на 14
max14, max7, max2, maxs = 0, 0, 0, 0
with open('../files/type2a.txt') as file:
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        num = int(text[i])
        if num % 14 == 0 and num > max14:
            max14 = num
        elif num % 7 == 0 and num > max7:
            max7 = num
        elif num % 2 == 0 and num > max7:
            max7 = num
        elif num > maxs:
            maxs = num
best_mult = max([max2, max7, maxs])
if max14 * best_mult > max2 * max7:
    print(max14 * best_mult)
else:
    print(max7 * max2)
