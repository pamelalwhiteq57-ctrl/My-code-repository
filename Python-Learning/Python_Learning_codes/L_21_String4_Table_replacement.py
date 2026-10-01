# print("先创建一个替换表格")
table = str.maketrans("ABCDEFG", "1234567")  # 就是将右边的字符依次替换为左边的字符
x = "ABCd567"
print(x.translate(table))  # 有table中左边同样字符的均被右边对应的字符替换
# print("也可直接在translate()中使用替换方法")
print()
Table = str.maketrans("ABCDEFG", "1234567", "ABC")  # 第三个参数表示需删除的字符
print(x.translate(Table))