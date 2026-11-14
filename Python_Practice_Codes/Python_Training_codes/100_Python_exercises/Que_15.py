# Question:15
'''
有一个已经排好序的数组a = [1,4,6,9,13,16,19,28,40,100]。现输入一个数，
要求按照原来的规律将它插入数组中
'''
a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
num = int(input("输入整数:"))
for i in range(len(a)):
    if num <= a[i]:
        a.insert(i, num)
        break
else:
    a.append(num)
print(a)