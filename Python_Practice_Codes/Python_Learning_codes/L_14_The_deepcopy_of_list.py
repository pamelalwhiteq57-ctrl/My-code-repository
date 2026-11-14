import copy
x = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
y = copy(x)
y = x[:]
y = copy.copy(x)
# print(y)
#这个三个运行的结果相同，都是浅拷贝

z = copy.deepcopy(x)
x[1][1] = 0
print(x)
print(y)
print(z)
#注意到进行深拷贝时，z不变，这与上一学习文件中的迭代法创建的列表相似