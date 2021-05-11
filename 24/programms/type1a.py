# Последовательность в которой каждый соседний символ отличен от текущего
with open('../files/type1a.txt') as file:
    text = file.read()
    prev = text[0]
    c = 0
    mc = 0
    for i in range(2, len(text) - 1):
        cur = text[i]
        next = text[i + 1]
        if prev != cur and cur != next:
            if c == 0:
                c = 2
            else:
                c += 1
        elif prev != cur:
            c += 1
            if c > mc:
                mc = c
                print(c, i)
            c = 0
        prev = cur
