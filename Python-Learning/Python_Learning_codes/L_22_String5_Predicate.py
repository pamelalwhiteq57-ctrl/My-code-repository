# print("startswith()用于判断字符串是否以指定的子字符串开头")
x = "Hello"
print(x.startswith("H"))
print(x.startswith("H", 1, 5))
print(x.startswith("H", 0, 5)) # 3，5行效果相同
print()
# print("endswith()用于判断字符串是否以指定的子字符串结尾")
print(x.endswith("o"))
print(x.endswith("o", 0, 4))
print(x.endswith("o", 0, 5)) # 8，10行效果相同
print()