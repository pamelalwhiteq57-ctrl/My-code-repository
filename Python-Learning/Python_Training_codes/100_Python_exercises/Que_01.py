# Question:1
'''
有1, 2, 3, 4四个数字，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

digits = [1, 2, 3, 4]
nums = []
for i in digits:
    for j in digits:
        if j == i:
            continue
        for k in digits:
            if k == i or k == j:
                continue
            nums.append(i * 100 + j * 10 + k)
counts = len(nums)
print(f"答:能组成{counts}个元素\n各是:", nums)