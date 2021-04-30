# Примечание:
# В этом подтипе числа в сумме должны иметь разные остатки от деления на d (160) и одноиз них должно делиться на p(7)

with open('../files/type5b.txt') as file:
    m1, m2 = 0, 0
    ms = 0
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        num = int(text[i])
        for j in range(i + 1, cnt + 1):
            num2 = int(text[j])
            # Все различие в этом условии
            # Поэтому медленный вариант в этом случае является лучшим, так как является гибким и подстраиваемым
            if abs(num - num2) % 160 !=0 and (num % 7 == 0 or num2 % 7 == 0) and num + num2 > ms:
                ms = num + num2
                m1, m2 = num, num2
print(m1, m2)
