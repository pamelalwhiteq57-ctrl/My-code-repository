class Turtle:
    def say(self):
        print("Go!")
class Cat:
    def say(self):
        print("Miao")
class Pup:
    def say(self):
        print("Bark")
class Garden:
    t: Turtle = Turtle()
    c: Cat = Cat()
    d: Pup = Pup()
    def say(self):
        self.t.say()
        self.c.say()
        self.d.say()
g: Garden = Garden()
print(g.say())
print()
class C:
    def set_x(self, v):
        self.x = v
c: C = C()
print(c.__dict__)  # c中无属性，为空字典
c.set_x(3)
print(c.__dict__)  # 发现其自己获得了一个名为x的新属性，值便是参数v
print()
class G:
    n = 1
g: G = G()
G.n = 10
print(g.n)  # 对象的属性随着其类的改变一起改变了
g.n = 2
G.n = 10
print(g.n)  # 注意到，单独修改对象的属性后，类的修改不再有效，仍以对象本身属性为优先级