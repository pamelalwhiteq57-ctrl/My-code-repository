# print("startswith()用于判断字符串是否以指定的子字符串开头")
x = "Hello"
print("以下为startswith的结果")
print(x.startswith("H"))
print(x.startswith("H", 1))
print(x.startswith("H", 0)) # 3，5行效果相同
print("以下为endswith的结果")
# print("endswith()用于判断字符串是否以指定的子字符串结尾")
print(x.endswith("o"))
print(x.endswith("o", 0, 4))
print(x.endswith("o", 0, 5)) # 8，10行效果相同
print("以下为startswith和endswith在元组判定情况下的结果")
# print("注意，可以用元组的形式写入多个子字符串，startswith()和endswith()方法会判断是否以元组中的任意一个子字符串开头或结尾")
print(x.startswith(("H", "h")))
print(x.endswith(("o", "O")))
print("以下为istitle的结果")
# print("istitle()用于判断字符串是否以大写字母开头且后续字母是否全为小写")
y = "Hello world"
print(x.istitle())
print(y.istitle())
print("以下为isupper的结果")
# print("isupper()用于判断字符串是否全为大写字母")
print(x.isupper())
print(x.upper().isupper())
print("以下为islower的结果")
# print("islower()用于判断字符串是否全为小写字母")
print(x.islower())
print(x.lower().islower())
print("以下为isalpha的结果")
# print("isalpha()用于判断字符串是否全为字母")
z = "你好"
print(x.isalpha())
print(y.isalpha()) # y中有空格，所以返回False
print(z.isalpha()) # z中全是Unicode汉字，所以返回True
print("以下为isspace的结果")
# print("isspace()用于判断字符串是否全为空白字符")
a = "     \t\n"    # 转义字符也是空白字符
print(a.isspace())
print("以下为isprintable的结果")
# print("isprintable()用于判断字符串是否全为可打印字符")
print("Hello".isprintable())
print("Hello\n".isprintable())  # 转义字符\n不是可打印字符
# print("isalnum()用于判断字符串是否全为字母和数字,详情见L_23")