def fx():
    x = 1
    def fy():
        x = 2
        print("In fy, x =", x)
    fy()
    print("In fx, x =", x)
# print("内部函数无法直接被调用，若需要fy()，需在外函数内(第6行)使用一次")
fx()
# print("外部函数的变量在内部函数中可被访问，但不能被修改，也只在当前区域生效")
print()
def fg():
    x = 1
    def fh():
        nonlocal x  # 使用nonlocal语句可以使外部函数中的变量在内部中被修改
        print(x)
    fh()
    print(x)
fg()
print()
print("LEGB规则，代表了变量作用域取的优先顺序，顺序为Local, Enclosed, Global, Build-In")