print("构造函数")
class N:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y
a: N = N(2, 3)
print(a.__dict__)
print(a.add(), a.mul())  # 即，__init__()的内容会在实例化结束时马上自动执行一次
print("重写")
class M(N):
    def __init__(self, x, y, z):
        N.__init__(self, x, y)  # super()指的就是父类中的构造函数(初始化方法)，用super()时不能写self参数
        self.z = z
    def add(self):
        return N.add(self) + self.z
    def mul(self):
        return N.mul(self) * self.z
b: M = M(2, 3, 4)
print(b.__dict__)
print(b.add(), b.mul())
print("钻石(菱形)继承的问题,super()函数后不能用self参数")
class A:
    def __init__(self):
        print("A here")
class B1(A):
    def __init__(self):
        super().__init__()  # 改为super()函数后解决
        print("B1 here")
class B2(A):
    def __init__(self):
        super().__init__()  # 改为super()函数后解决
        print("B2 here")
class C(B1, B2):
    def __init__(self):
        super().__init__()  # 改为super()函数
        # B2.__init__(self)
        print("C here")
c: C = C()
print(c)  # 发现类A的构造函数被调用两次，改为super()后恢复正常
# 用 print(C.mro()) 或 print(C.__mro__) 来查看MRO顺序