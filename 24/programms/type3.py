# Ищем кол-во строк в которых символов E больше чем символов A
with open('../files/type3.txt') as file:
    text = file.read().split('\n')
    c = 0
    for line in text:
        a, e = 0, 0
        for L in line:
            if L == 'A':
                a += 1
            elif L == 'E':
                e += 1
        if e > a:
            c += 1
print(c)
