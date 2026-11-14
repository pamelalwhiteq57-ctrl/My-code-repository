# print("函数作为参数时使用")
def fx():
    print("It is fx()")
def report(func):
    print("Using the function")
    fx()
print(report(fx))