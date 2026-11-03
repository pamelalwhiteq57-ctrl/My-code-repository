class S(str):
    def __add__(self, other):
        return len(self) + len(other)

    def __mul__(self, other):
        return len(self) * len(other)

    def __str__(self):
        return f"Custom String: {super().__str__()}"
s1: S = S("Hello")
s2: S = S("World")
print(s1 + s2)
print()
class C1(str):
    def __add__(self, other):
        return NotImplemented
class C2(str):
    def __radd__(self, other):
        return len(self) + len(other)
c1: C1 = C1("Hello")
c2: C2 = C2("World")
print(c1 + c2)
print()
print("在魔法方法前加上i， 就可以实现增强赋值运算的操作")
...
print()
# print("按位运算符:")
print("按位和运算符 &")
print(3 & 2)
print(bin(3 & 2))
print("按位或运算符 |")
print(3 | 2)
print(bin(3 | 2))
print("按位异或运算符 ^")
print(3 ^ 2)
print(bin(3 ^ 2))
print("按位取反运算符 ~")
print(~3)
print(bin(~3))
print("按位左移和右移运算符 <<, >>")
print(3 << 1)
print(bin(3 << 1))
print(3 >> 1)
print(bin(3 >> 1))
print()
print("__index__() 魔法方法: 通过索引获取对象的值")
class MyInt:
    def __index__(self):
        print("调用了 __index__() 方法")
        return 3
m: MyInt = MyInt()
# m[0]  # 不能直接使用数字索引
s = "Hello"
s[m]  # 使用 MyInt 对象作为索引, 才能拦截, 并调用__index__() 方法
print(bin(m))