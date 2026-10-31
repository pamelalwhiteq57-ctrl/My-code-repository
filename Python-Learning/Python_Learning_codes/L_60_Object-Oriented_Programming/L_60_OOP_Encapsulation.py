# print("使用class关键字创建一个类，属性，就是其中的变量；方法，就是其中的函数")
class Turtle:
    head = 1
    eyes = 2
    legs = 4
    shell = True
    def crawl(self):
        print("C")
    def run(self):
        print("R")
    def bite(self):
        print("B")
    def eat(self):
        print("E")
    def sleep(self):
        print("Zzzzz...")
t1: Turtle = Turtle()
t2: Turtle = Turtle()
print(t1.head, t1.legs, t1.crawl(), t1.bite())  # 遇到函数直接打印，先出结果
print()
# print("对象的属性可以随时修改，而来自同一个类的其他对象不会被影响")
t1.legs = 3
print(t1.legs, t2.legs)
# print("可以动态地为一个对象创建一个属性")
t1.mouth = 1
print()
# print(dir(t1))
# print(dir(t2))