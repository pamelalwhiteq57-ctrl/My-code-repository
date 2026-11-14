# Question:14
'''
使用冒泡对数组进行排序
'''
a = [6, 8, 2, 5, 15, 10, 1, 7, 3]
n = len(a)
for i in range(n):
    swapped = False
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped:
        break
print(a)