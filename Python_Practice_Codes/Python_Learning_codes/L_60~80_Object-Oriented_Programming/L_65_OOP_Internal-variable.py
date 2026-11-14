class C:
    def __init__(self, x):
        self.__x = x      # 伪私有变量
    def set_x(self, x):
        self.__x = x      # 伪私有变量
    def get_x(self):
        return self.__x
c: C = C(200)
# print(c.__x)  # 发现报错无法访问
print(c.get_x())  # 通过内部方法可以访问到它的数据
print(c.set_x(100))
print(c.get_x())
print(c.__dict__) # __dict__也能看到其属性
# print("对象直接访问法: _加上类名再加上属性名")
print(c._C__x)
print()
# print("方法也能改为隐藏")
class D:
    def __func(self):
        return "Hello"
d: D = D()
# print(d.__func())  # 发现无法调用
print(d._D__func())  # 但也可通过 ._C__func 的形式调用(不建议)