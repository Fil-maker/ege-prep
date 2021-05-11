# Примечание:
# В этом подтипе ищем кол-во пар, удовлетворяющих условию

with open('../files/type5c.txt') as file:
    pairs = 0
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        num = int(text[i])
        for j in range(i + 1, cnt + 1):
            num2 = int(text[j])
            if (num + num2) % 80 == 0 and (num > 50 or num2 > 50):
                pairs += 1
print(pairs)
