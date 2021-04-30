# Примечание: Данный алгоритм не эталон, так как выполнятеся слишком,
# ввиду того что просматривает абсолютно все пары чисел. Его можно оптимизировать исключив повторяющиеся элементы,
# что тяжело и может не сработать или разбив на два массива в одном из которых будут все четные, а в другом нечетные
# по моим подсчетам такой алгоритм будет на 20%-30% быстрее, что может сыграть. Однако на экзамене важна программа не,
# а результат. Такой код тоже код

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