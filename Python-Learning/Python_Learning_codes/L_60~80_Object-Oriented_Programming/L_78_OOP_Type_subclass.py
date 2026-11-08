print(type(3)("4"))
print(type([])("Python"))
print(type({}).fromkeys("ABC", 1))
print()
class C:
    def __init__(self, x):
        self.x = x
c: C = C(3)
d = type(c)(520)
print(c)
print(d)
print(c.__class__)
print(d.__class__)
print()
print(type(C))
print(type(type))  # 类也是一种对象,type自身就是自身的对象
print()  # 用type创造一个新的类
class C:
    pass
C = type('C', (), {})
c: C = C()
print(c.__class__)
print(C.__bases__)  # 查看父类，任何最初类的父类都是object
D = type('D', (C,), {})
print(D.__bases__)
E = type('E', (), dict(x=2, y=5))
print(E.x)
def funC(self, name="Abby"):
    print(f"Hi, {name}")
F = type('F', (), dict(say_hi=funC))
f: F = F()
f.say_hi()
f.say_hi("Nocturne")
print()
class C:
    def __init_subclass__(cls):
        print("父类的此方法已自动触发(有以这个类为父类的子类定义完成),打印此句")
        cls.x = 520
class D(C):
    x = 3
print(D.x)
print("kwds参数与__init_subclass__")
