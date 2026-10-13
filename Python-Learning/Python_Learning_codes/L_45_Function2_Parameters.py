# print("自定义函数中，位置参数必须在关键字参数前")
# print("默认参数，是在实参未传入时默认传入的参数，例")
def fx(sub, obj, pre="love"):
    return f"{sub} {pre} {obj}"
print(fx("I", "Python"))
# print("可以单独使用一个/参数来区分开位置参数与关键字参数，/左边不支持关键字参数")