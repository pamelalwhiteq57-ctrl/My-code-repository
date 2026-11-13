# Question:34
'''
定义一个父类Square表示正方形，并定义一个计算面积的函数，然后定义多个子类Rectangle，Circular，Triangle
分别表示长方形，圆，正三角形，并重写面积计算方法。
根据输入的图形及边长(圆为半径)计算其面积(三角形与圆的面积保留三位小数)
例:
输入: Square
      4
输出:16
'''
import math
class Square:
    def __init__(self, side):
        self.side = side
    @property
    def area(self) -> float:
        return self.side * self.side
class Rectangle(Square):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self) -> float:
        return self.length * self.width
class Circular(Square):
    @property
    def area(self):
        return float(self.side * self.side * math.pi)
class Triangle(Square):
    @property
    def area(self):
        return float(self.side ** 2 * math.sqrt(3) / 2 / 2)
shape = input().strip()
dimensions = input().strip()
if shape == "Square":
    print(Square(int(dimensions)).area)
elif shape == "Rectangle":
    width, height = map(int, dimensions.split())
    print(Rectangle(width, height).area)
elif shape == "Circular":
    res = Circular(float(dimensions)).area
    print(f"{res:.3f}")
else:
    result = Triangle(float(dimensions)).area
    print(f"{result:.3f}")