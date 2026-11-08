class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
rectangle = Rectangle(5, 2)
print(rectangle.length)
print(rectangle.width)
print(rectangle.area)  # 发现，area能被随时更改
print("若使用修改类的定义的方法")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
print()
print("用@property装饰器法")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width
print(rectangle.length)
print(rectangle.width)
print(rectangle.area)