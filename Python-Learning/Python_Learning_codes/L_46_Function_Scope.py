# print("作用域指某个变量可以被访问的范围")
def fx():
    x = 3
    print(x)
print(fx())
print()
# 但print(x)报错，∵变量被定义到了函数内部
# print('''
# 局部作用域:在函数中定义的变量叫局部变量，其的作用范围
# 全局作用域:在外部定义的叫全局变量，其的作用范围''')
# print("当一个局部变量和全局变量同名时，它们互不影响，但局部变量会优先覆盖全局变量，它们本质也是两个变量")
# print("但全局变量可以在函数中被访问，但无法修改它的值")
y = 333
def fy():
    y = 444
    print(id(y))
print(id(y))
fy()  # 两者id不同
print()
# print("使用globle语句可以使得在函数内部修改全局变量的值")
z = 30
def fz():
    global z
    z = 50
    print(z)
fz()
print(z)  # 注意到最终结果已被改变