# print("自定义函数中，位置参数必须在关键字参数前")
# print("默认参数，是在实参未传入时默认传入的参数，例")
def fx(sub, obj, pre="love"):
    return f"{sub} {pre} {obj}"
print(fx("I", "Python"))
# print("可以单独使用一个/参数来区分开位置参数与关键字参数，/左边不支持关键字参数")
# print("用*作为参数来区分时，*使得右侧定义的参数必须是关键字参数")
print()
# print("定义收集参数的方法，在参数前加上*，若后续需要定义使用其他参数，必须是关键字参数")
def fy(*args):
    print("有{}个参数".format(len(args)))
    print("第2个参数是:{}".format(args[1]))
print(fy(1, 2, 3, 4, 5))
print()
# print("将return结果打包为字典的方法:'**'，此时参数就是键，∴必须使用关键字参数例")
def fz(**keyword):
    print(keyword)
print(fz(A=1, B=2, C=3))
print()
def fg(a, *b, **c):
    print(a, b, c)
print(fg(1, 2, 3, 4, x=5, y=6))
print()
# print("解包参数，即*和**在实参上的应用")
args = (1, 2, 3, 4)
def fh(a, b, c, d):
    print(a, b, c, d)
# print("若直接把元组args放入，会报错，这时便需要解包这个待传入参数，在实参处加上*即可，且长度必须相同")
print(fh(*args))
# print("同理，在传入字典类型的实参时，加上'**'即可解包")
dic = {'a':1, 'b':2, 'c':3, 'd':4}
print(fh(**dic))