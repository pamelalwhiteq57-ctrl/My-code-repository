# print("定义一个函数，def+函数名()，\\n后为被打包的代码块")
def name():
    pass
print(name())
# print("定义函数参数，例")
def fx(nam, times):
    for i in range(times):
        print(f"I like {nam}.")
print(fx("Coding", 3))
# print("定义函数时，参数名叫形式参数，是占位符，用于接收数据；调用时传入的叫实际参数，是真正交给函数的参数值")
print()
# print("函数的返回值，用return语句，无return或未执行成功return默认返回None，例")
def div(x, y):
    if y == 0:
        return "Error!"
    else:
        return x / y
u = div(9, 0)
print(u)
# print("return时，函数会立刻返回结果而忽略其他语句，∴例的结果与上是相同的")
def divi(x, y):
    if y == 0:
        return "Error!"
    return x / y
o = divi(9, 0)
print(o)