# № 33497
with open('../files/type1b.txt') as file:
    msr, s1, s2 = 0, 0, 0
    min_dif = 10000
    text = file.read().split('\n')
    cnt = int(text[0])
    for i in range(1, cnt + 1):
        nums = sorted([int(n) for n in text[i].split()])
        # Не важно какие числа мы добавляем в другие 2 списка.
        s1 += nums[0]
        s2 += nums[1]
        msr += nums[2]
        dif1, dif2 = nums[2] - nums[1], nums[2] - nums[0]
        if dif1 % 2 != 0 and dif1 < min_dif:
            min_dif = dif1
        if dif2 % 2 != 0 and dif2 < min_dif:
            min_dif = dif2
# Если оба списка четны или не четны, то вычитаем из результата минимальную разницу,
# необходимую для достижения результата
if s1 % 2 == s2 % 2:
    print(msr - min_dif)
else:
    print(msr)
