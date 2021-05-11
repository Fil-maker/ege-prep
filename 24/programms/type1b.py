# Ищем длинну наибольшей подстроки, в которой все символы одинаковы
with open('../files/type1b.txt') as file:
    text = file.read()
    prev = text[0]
    c = 0
    mc = 0
    for i in range(len(1, len(text))):
        cur = text[i]
        if prev == cur:
            if c == 0:
                c = 2
            else:
                c += 1
        else:
            if c > mc:
                mc = c
