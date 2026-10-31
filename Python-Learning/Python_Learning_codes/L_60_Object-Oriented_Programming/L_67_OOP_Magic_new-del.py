# # print("__new__(cls [, ...] 方法)")
# class Phone:
#     def __new__(cls, *args, **kwargs):
#         print("1. 执行 __new__，开始造手机")
#         # 调用父类 object 的 __new__ 来真正创建对象
#         instance = super().__new__(cls)
#         return instance  # 必须把造好的对象交出去！
#     def __init__(self, brand):
#         print("2. 执行 __init__，开始装系统")
#         self.brand = brand
# p = Phone("Apple")
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)  # 返回的必须是一个对象
cs: CapStr = CapStr("Ewevdn")
print(cs)
print(cs.capitalize())  # __new__只是定义了一个构造方法，后续仍可修改
print()
class C:
    def __init__(self):
        print("I'm coming")
    def __del__(self):
        print("I'm leaving")
c: C = C()
del C  # 但如果此时类还绑定着其他对象，则不会出发__del__()，必须全删完才会