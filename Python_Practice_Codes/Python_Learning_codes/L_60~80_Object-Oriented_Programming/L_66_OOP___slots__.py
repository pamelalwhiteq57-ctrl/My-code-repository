class C:
    __slots__ = ["x", "y"]  # 表名这个类的属性名限制，只能有__slots__中元素的才行
    def __init__(self, x):
        self.x = x
c: C = C(60)
print(c.x)
c.y = 80
print(c.x, c.y)
# c.z = 40  # 不在__slots__范围内的动态添加是不能成功执行的
print("从内部跳脱出__slots__的范围也是错的，形如self.x的属性赋值仍不能超过其范围")
print("如，以上例，若__init__的参数为(self,x,y,z)并self.z=z, 这是错的")