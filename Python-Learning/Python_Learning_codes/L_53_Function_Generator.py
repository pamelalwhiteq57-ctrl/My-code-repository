def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
# print("使用yield替换return后，得到的不是返回值，而是生成器0")
# print("可通过for来使用这个生成器")
for i in counter():
    print(i)
print()
# print("生成器在每次调用时提供一个数据，yield就负责暂停并保留状态")
c = counter()
next(c)
next(c)
next(c)
next(c)
next(c)
d = next(c)  # 这是第6次next，所以得到5
print(d)
print()
# print("使用生成器输出斐波那契数列的前10项值")
def fib():
    b1, b2 = 0, 1
    while True:
        yield b1
        b1, b2 = b2, b1 + b2
for index, j in enumerate(fib()):
    if index == 10:
        break
    print(j)
print()
# print("生成器表达式，简单例子")
t = (i ** 2 for i in range(5))
for j in t:
    print(j)