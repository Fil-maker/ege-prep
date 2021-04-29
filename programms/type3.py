# Будем искать кол-во пар числе, произведение которых делится на 26
with open('../files/type3.txt') as file:
    text = file.read().split('\n')
    cnt = int(text[0])
    count2, count13, count26 = 0, 0, 0
    for i in range(1, cnt + 1):
        num = int(text[i])
        if num % 26 == 0:
            count26 += 1
        elif num % 13 == 0:
            count13 += 1
        elif num % 2 == 0:
            count2 += 1
print(count2 * count13 + count26 * (count26 - 1) / 2 + count26 * (cnt - count26))
