def squareX(x):
    return x * x
squareY = lambda y : y * y
print(squareX(3))
print(squareY(3))
print()
# print("lambda又称匿名函数，通过赋给一个变量的方式将其存储，以及后续调用")
# print("∵lambda是一个表达式，∴可以放入普通函数无法放入的位置如列表中")
y = [lambda x : x * x, 2, 3]
for i in range(3):
    print(y[i])  # 发现其可作为元素使用
print()
print(y[0](y[1]))  # 把第二个元素作为参数传入通过下标索引调用的lambda表达式中