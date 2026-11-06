class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"这是一个向量，坐标是 ({self.x}, {self.y})"
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v = Vector(3, 4)
# 触发 __str__
print(v)        # 输出: 这是一个向量，坐标是 (3, 4)
print(str(v))   # 输出: 这是一个向量，坐标是 (3, 4)
# 触发 __repr__
print(repr(v))
# 💡 最直观的区别在这里：
# 当你在 VSCode 终端里，直接敲 v 回车，或者在列表里打印它时：
v_list = [v, v]
print(v_list)   
# 输出: [Vector(3, 4), Vector(3, 4)]  <-- 注意，列表打印对象时，用的是 __repr__！
class LazyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"LazyClass('{self.name}')"
l = LazyClass("Abby")
print(l)      # 输出: LazyClass('Abby') （没写 __str__，自动借用 __repr__）