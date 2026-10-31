class A:
    x = 520
    def hello(self):
        return ("Hello, I'm A~")
# print("以A为父类，创建一个其子类B方法")
class B(A):
    ...
print(A is B)  # 虽然属性方法都相同，但仍是不同的类
print()
b: B = B()
print(b.x, b.hello())
print()
# print("若子类里存在其父类中同名的属性或方法")
class C(A):
    x = 8
    def hello(self):
        return ("Hello, I'm C~")
c: C= C()
print(c.x, c.hello())  # 发现子类中的属性和方法优先级更高
print(isinstance(c, C), isinstance(c, A))  # 发现父类的属性仍然包含
print(issubclass(B, A), issubclass(A, C))  # 判断前者是否是后者的子类
print()
# print("多重继承，继承的父类属性和方法的优先级是从左往右的")
class D:
    x = 666
    def hello(self):
        return "Hello, I'm D~"
class E:
    x = 9
    y = 9
    def hello(self):
        return "Hello, I'm E~"
class F(D, E):
    ...
f: F = F()
print(f.x, f.y, f.hello())  # 发现属性和方法优先级是左边父类的高，但右边的父类同样能生效，只是优先级更低
