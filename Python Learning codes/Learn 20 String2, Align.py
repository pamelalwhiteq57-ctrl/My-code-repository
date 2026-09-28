# print("center()是对其左右进行填充，填充数为输入的数字-原字符串长度值，且先右后左:")
x = "123456789"
x = x.center(13)
print(x)
print()
# print("ljust()是让其实现左对齐(往左靠)，填充数为输入的数字-原字符串长度值:")
y = "123456789"
y = y.ljust(13)
print(y)
print()
# print("rjust()是让其实现右对齐(往右靠)，填充数为输入的数字-原字符串长度值:")
z = "123456789"
z = z.rjust(13)
print(z)
print()
# print("zfill()是用'0'去填充左侧(有'-'在前面时，会自动跳过它):")
i = "-123456789"
i = i.zfill(13)
print(i)
print()
# print(除了zfill()，其余的都可以在长度后加上想要填充的内容，如:)
j = "123456789"
j = j.center(10, "q")
print(j)