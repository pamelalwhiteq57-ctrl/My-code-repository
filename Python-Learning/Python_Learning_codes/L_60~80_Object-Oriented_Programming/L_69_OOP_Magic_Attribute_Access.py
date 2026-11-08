class User:
    def __init__(self):
        self.name = "张三"

    # 兜底方法
    def __getattr__(self, name):
        print(f"⚠️ 警告：属性 {name} 不存在，已返回默认值。")
        return None

u = User()
print(u.name)    # 正常输出：张三
print(u.age)     # 输出：⚠️ 警告：属性 age 不存在，已返回默认值。 None
print()
class User:
    def __init__(self):
        self.name = "张三"

    def __getattribute__(self, name):
        print(f"有人试图访问属性：{name}")
        # ⚠️ 必须用 super() 交还给父类去实际干活，否则死循环！
        return super().__getattribute__(name) 

u = User()
print(u.name) 
# 输出：
# 有人试图访问属性：name
# 张三
print()
class Person:
    def __init__(self, age):
        self.age = age  # 这一步就会触发 __setattr__

    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("年龄不能为负数！")
        # ⚠️ 必须用 super() 真正把值存进去，否则赋值失败！
        super().__setattr__(name, value)

p = Person(18)
print(p.age)    # 18

p.age = -5      # 报错：ValueError: 年龄不能为负数！
print()
class Fake:
    def __getattr__(self, name):
        return "假装有这个属性"

f = Fake()
print(hasattr(f, "外星人")) # 输出 True（因为 __getattr__ 没报错）