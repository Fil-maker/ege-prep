# Ищем самую часто встречающуюся букву в строке с наибольшим кол-вом букв N


with open('../files/type5.txt') as file:
    text = file.read().split('\n')
    mc = 0
    md = {}
    for line in text:
        cort = {}
        c = 0
        for L in line:
            cort[L] = cort.get(L, 0) + 1
            if L == 'N':
                c += 1
        if (c < mc or mc == 0) and c != 0:
            mc = c
            md = cort
# Здесь я смотрю на то какая буква должна попасть в ответ, однако на самом экзе никто не мешает сделать это самому
let, con = None, None
for key, val in sorted(md.items(), key=lambda x: md[x[0]], reverse=True):
    if let is None:
        let, con = key, val
    # Здесь используем тот факт, что сравнение символов происходит по их кодовым словам. В этом случае
    # кодовое слово буквы стоящей в алфавите дальше больше. (с несколькими алфавитами такое слабо прокатит)
    elif val == con and key > let:
        print(key)
        let = key
print(let)
