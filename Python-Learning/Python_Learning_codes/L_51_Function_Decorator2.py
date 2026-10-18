# print("装饰器的参数")
import time

def logger(msg):
    def time_calculate(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共花费了 {(stop - start):.2f}")
        return call_func
    return time_calculate

@logger(msg="A")
def fx():
    time.sleep(1)
    print("正在调用fx()")

@logger(msg="B")
def fy():
    time.sleep(1)
    print("正在调用fy()")

fx()
fy()
print()
# print('''本质等于:
# fx = logger(msg="A")(fx)
# fy = logger(msg="B")(fy)''')