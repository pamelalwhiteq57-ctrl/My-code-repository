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
