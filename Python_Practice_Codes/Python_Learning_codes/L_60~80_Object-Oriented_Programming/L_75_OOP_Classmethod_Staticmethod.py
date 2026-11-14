print("类方法")
class C:
    def funA(self):
        print(self)
    @classmethod
    def funB(cls):
        print(cls)
c: C = C()
print(c.funA())
print(c.funB())
print()
class C:
    count = 0
    @classmethod
    def add(cls):
        cls.count += 1
    def __init__(self):
        self.add()
    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了 {cls.count} 个对象")
c1 = C()
c2 = C()
c3 = C()
c3.get_count()
c3.count = 1
print(c3.count)
print(c3.get_count())  # 发现不受影响，因为类方法里面的指定对象是cls
print()
print("静态方法")
class C:
    @staticmethod
    def funC():
        print("I love Python")
c: C = C()
c.funC()
print()  # 类似于上面类方法的使用法，本质都是让对象不与其产生联系
class C:
    count = 0
    def __init__(self):
        C.count += 1
    @staticmethod
    def get_count():
        print(f"该类一共实例化了 {C.count} 个对象")
c1 = C()
c2 = C()
c3 = C()
c3.get_count()