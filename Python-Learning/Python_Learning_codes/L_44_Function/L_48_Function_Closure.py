# print("闭包")
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
square = power(2)  # exp变为2的exp_of()函数，即指数为2，再次调用即可决定底数
cube = power(3)   # 同理，此时外部函数的作用域已被记下，可继续参与后续内部函数的调用
print(square(2), cube(2))
print()
# print("利用内层函数能记下外层函数变量的规则")
def outer():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"Now, x = {x}, y = {y}")
    return inner
use = outer()  # 此时，use变为内部函数inner()本身，但同时∵nonlocal，也会记录外层x,y的值
use(1, 2)
use(-2 ,2)  # 注意到结果是与第21行的结果有联系的