k = 3
with open('../files/type1.txt') as file:
    text = file.read().split('\n')
    cnt = int(text[0])
    min_dif = None
    max_sum = 0
    for st in range(1, cnt + 1):
        string = text[st]
        # Существуют подтипы, в которых нужно найти минимальную сумму. В таком случае параметр reverse должен быть True
        nums = sorted([int(i) for i in string.split()])
        max_sum += max(nums)
        dif = nums[1] - nums[0]
        if nums[1] % k != nums[0] % k or min_dif is None:
            min_dif = dif
print(max_sum, max_sum - min_dif)
