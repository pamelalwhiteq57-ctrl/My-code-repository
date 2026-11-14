# Question:17
'''
两个3行3列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
'''
x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
def calculate(m1, m2):
    temp = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    temp1 = temp
    for i in range(3):
        for j in range(3):
            temp1[i][j] = m1[i][j] + m2[i][j]
    return temp1
print(calculate(x, y))
def func(m1, m2):
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(m1, m2)]
print(func(x, y))