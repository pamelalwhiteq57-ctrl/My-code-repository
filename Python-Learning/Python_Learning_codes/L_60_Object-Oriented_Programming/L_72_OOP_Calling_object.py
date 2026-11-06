class C:
    def __call__(self):
        return "Hi"
c: C = C()
print(c())
print()
class MyCalculator:
    # 实现 __call__ 方法，接收任意参数
    def __call__(self, *args, **kwargs):
        print("收到的位置参数 (*args):", args)
        print("收到的关键字参数 (**kwargs):", kwargs)
calc = MyCalculator()
calc(1, 2, 3, 名字="Abby", 年龄=19)
print()
class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
    def __delattr__(self, name):
        # 1. 拦截：如果是核心属性，直接拒绝
        if name == "id":
            raise AttributeError("❌ 核心属性 id 绝不允许被删除！")
        print(f"✅ 准备删除属性: {name}")
        # 2. 放行：调用父类真正删除
        super().__delattr__(name)
u = User(1001, "张三")
del u.name       # 输出: ✅ 准备删除属性: name
del u.id         # 报错: AttributeError: ❌ 核心属性 id 绝不允许被删除！