class MetaC(type):
    pass
class C(metaclass=MetaC):
    pass
c: C = C()
print(type(c))
print(type(C))
print(type(MetaC))  # 元类介于类与type之间，类可以通过metaclass继承自某个元类
print()
class MetaC(type):
    def __new__(mcls, name, bases, attrs):
        print("__new__() in MetaC")
        return type.__new__(mcls, name, bases, attrs)
    def __init__(cls, name ,bases, attrs):
        print("__init__() in MetaC")
        type.__init__(cls, name, bases, attrs)
class C(metaclass=MetaC):
    def __new__(cls):
        print("__new__() in C")
        return super().__new__(cls)
    def __init__(self):
        print("__init__() in C")
c: C = C()