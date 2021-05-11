# Ищем самую часто встречающуюся букву после A

cort = {}
with open('../files/type4a.txt') as file:
    text = file.read()
    for i in range(1, len(text)):
        sli = text[i - 1:i + 1]
        if sli[0] == 'A':
            # Эта штука прибавляет 1 в значение буквы
            cort[sli[1]] = cort.get(sli[1], 0) + 1

vals = list(cort.values())
keys = list(cort.keys())
print(keys[vals.index(max(vals))])
