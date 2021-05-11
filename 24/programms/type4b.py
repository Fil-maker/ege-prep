# Ищем самую часто встречающуюся букву после двух одинаковых
cort = {}
with open('../files/type4b.txt') as file:
    text = file.read()
    for i in range(1, len(text)):
        sli = text[i - 1:i + 2]
        if sli[0] == sli[1]:
            # Эта штука прибавляет 1 в значение буквы
            cort[sli[2]] = cort.get(sli[2], 0) + 1

# А здесь достаем эту букву
vals = list(cort.values())
keys = list(cort.keys())
print(keys[vals.index(max(vals))])
