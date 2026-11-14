def report(cls):
    def oncall(*args, **kwargs):
        print("开始实例化对象")
        _ = cls(*args, **kwargs)
        print("完成实例化")
        return _
    return oncall
@report
class C:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("__init__生效")
c: C = C(1, 2 ,3)
print()
class Counter:
    def __init__(self, func):
        self.count = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.count += 1
        print("已调用 %d 次"%(self.count))
        return self.func(*args, **kwargs)
# c: C = Counter()
# c()
@Counter
def say_hi():
    print("Hi")
say_hi()