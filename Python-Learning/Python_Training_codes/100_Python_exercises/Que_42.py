# Question:42
'''
生成斐波那契数列
'''
def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
n = int(input("输入想查看的斐波那契数列项数:"))
for index, j in enumerate(fib()):
    if index == n:
        break
    print(j)