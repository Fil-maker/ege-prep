# Ищем макс дилнну подстроки состоящей из символов AB
# Было лень реализовывать этот алгоритм так как надо, а потому сделал так как работает
with open('../files/type2.txt') as file:
    text = file.read()
    prev = text[:2]
    c, mc = 0, 0
    cur1 = ''
    cur2 = ''
    for i in range(0, len(text) - 2, 2):
        cur = text[i:i + 2]
        if cur == 'AB':
            cur1 += cur
        elif text[i] == 'A':
            cur1 += 'A'
            if len(cur1) > mc:
                mc = len(cur1)
                print(cur1, len(cur1))
            cur1 = ''
    for i in range(1, len(text) - 3, 2):
        cur = text[i:i + 2]
        if cur == 'AB':
            cur2 += cur
        elif text[i] == 'A':
            cur2 += 'A'
            if len(cur2) > mc:
                mc = len(cur2)
                print(cur2, len(cur2))
            cur2 = ''

print(mc)
