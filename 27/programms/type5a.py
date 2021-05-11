# Ищем два числа разность которых кратна 2, сумма максимальна и одно из них делится на 17

with open('../files/type5a.txt') as file:
    m1, m2 = 0, 0
    ms = 0
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        num = int(text[i])
        for j in range(i + 1, cnt + 1):
            num2 = int(text[j])
            if abs(num - num2) % 2 == 0 and num + num2 > ms and (num % 17 == 0 or num2 % 17 == 0):
                ms = num + num2
                m1, m2 = num, num2
print(m1, m2)


# Примечание: Данный алгоритм не super good
# ввиду того что просматривает абсолютно все пары чисел. Его можно оптимизировать.
# Однако на экзамене важна не программа, а результат. Такой код тоже код.
