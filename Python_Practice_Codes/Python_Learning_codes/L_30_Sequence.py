# print("Python把列表，元组和字符串统称为序列\n其中，列表为可变序列，元组和字符串为不可变序列")
# print("对以下列表进行增量运算后，发现id()的值相同，id()返回的是一个对象的唯一标志")
# print("唯一标志是随着对象创建时就有的")
s = [1, 2, 3]
print(id(s))
s *= 2
print(id(s))
print()
# print("但对于不可变序列，如元组，发现增量运算后唯一标志改变")
t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))
print()
# print("同一性运算符'is'和'is not'，判断俩对象id值是否相等/不等")
# print("如L_13,14,15中所提，俩变量的列表即使元素完全相同，id也不同; 字符串则相反，内容相同id也相同")
x, y = "123", "123"
print(x is y)
a, b = [1, 2, 3], [1, 2, 3]
print(a is b)
print()
# print("'in'和'not in'用于判断某个元素是否包含在序列中")
print("Yes" in "YesNo")
print("YesNo" not in "Yes")
print()
# print("del语句，用于删除一个或多个指定对象，以及可变序列中的特定元素")
i, j = 1, 2
del i, j
c = [1, 2, 3, 4, 5]
del c[0:4]
print(c)
print()
d = [1, 2, 3, 4, 5]
print("del d[:]的效果等同于d.clear()")
del d[:]
print(d)