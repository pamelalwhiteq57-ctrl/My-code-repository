print("用iter()函数把可迭代对象变成迭代器")
x = [1, 2, 3, 4, 5]
y = iter(x)
print(type(x), type(y))
print()
print("用next()函数提取迭代器中的元素")
for i in y:
    print(i)
print("超出迭代范围时，可以用next()中的第二个参数决定超出范围输出的内容")
z = iter(x)
for j in range(6):
    result = next(z, "Done")
    print(result)