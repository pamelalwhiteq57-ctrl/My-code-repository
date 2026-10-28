# print("在函数的第一个语句使用"""三引号来编辑文档字符串)
def fx(a,b):
    """
    contents
    """
    return a + b
print()
# print("类型注释，即函数定义者期望传入的参数类型，在类型注释后可以通过=写上默认参数")
def times(s:str, n:int) -> str:
    return s * n
print(times("EWEVDN", 3))
def time(s:dict[str, int], n:int) -> list:
    return list(s.keys()) * n  # 期望让键来*n
print()
# print('''内省(小部分)
# 内置函数:
# help(), dir(), type(), callable()
# 特殊属性内省:
# ._name_        查看函数名
# ._annotation_  查看函数注释类型
# ._doc_         查看函数文档
# ._defaults_    查看函数默认参数值''')
print()