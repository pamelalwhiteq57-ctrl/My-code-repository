matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in matrix:
    for y in i:
        print(y, end = " ")
print()
print(matrix[0][1])
#类比为行和列
print()
#迭代法创建二维列表：
x = [0] * 3
#得到[0, 0, 0]
print(x)
for i in range(3):
    x[i] = [0] * 3
print(x)
print()
y = [[0] * 3] * 3
print(y)
#通过is来检测上下两种方式形成的二维列表中的内列表来发现区别，即储存的内存地址不同导致的
x[0][0] = 99
y[1] = [8, 8, 8]
y[0][0] = 99
#发现x[0][0]与x[1][0]结果不同
print(x)
print(y)