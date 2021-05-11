# Такая задача на решуегэ всего одна, но она обозначена как досрочное ЕГЭ 2021, так что покажу.
# Ищем максимальную длину подстроки, в которой нет XZZY


with open('../files/type6.txt') as file:
    text = file.read()
    cur = ''
    mc = 0
    for i in range(len(text)):
        L = text[i]
        if (cur + L).find('XZZY') == -1:
            cur += L
            # print(cur)
        elif (cur + L).find('XZZY') != -1:
            if len(cur) > mc:
                mc = len(cur)
            # здесь мы добавляем в подстроку поиска последние 3 символа последовательности, так как последние 4 содержат
            # XZZY
            cur = text[i - 2:i + 1]
print(mc)

# Примечание: задача так себе, решение тоже.
