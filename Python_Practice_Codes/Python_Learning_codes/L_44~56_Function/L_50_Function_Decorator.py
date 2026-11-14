# print("函数的装饰器，可以在不修改原函数的情况下，给函数加一层'功能'，例:")
import time
def time_calculate(func):
    def call_func():
        start = time.time()
        func()
        stop = time.time()
        print(f"消耗了{(stop - start):.2f}秒")
    return call_func
# print("这是一个计算函数运行时间的程序，若想在执行待测函数后自动且立刻用此函数进行计算，就需要装饰器了")

@time_calculate
def fx():
    time.sleep(2)  # 让时间计算加2秒(程序休眠2秒)
    print("Calculating")
print(fx())
# print("每次使用fx()时，都会返回装饰器函数的结果")
print("@是语法糖，本质其实就是time_calculate(fx())的结果")
# printi("有多个修饰器时，先调用最下方离定义函数最近的@装饰器函数")