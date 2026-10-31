class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
class Square(Shape):
    def __init__(self, length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length * self.length
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("三角形")
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2
s: Square = Square(5)
c: Circle = Circle(6)
t: Triangle = Triangle(3, 4)
print(s.name, c.name, t.name)
print(s.area(), c.area(), t.area())
print()
def calculate(x):
    return x.area()
print(calculate(s), calculate(c), calculate(t))  # 多态的应用