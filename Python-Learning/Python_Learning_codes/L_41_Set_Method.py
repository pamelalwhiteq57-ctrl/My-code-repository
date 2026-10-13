s = {1, 2, 3}
g = s.copy()  # 浅拷贝方法
print(s, g)
print()
# print("isdisjoint()方法检测俩集合是否不相干(有交集)")
print(s.isdisjoint(set("123")))  # 无关，∴返回True
print(s.isdisjoint("123"))  #同样无关，∴返回True
print(s.isdisjoint({2, 1}))  # ∵有交集。∴有关，∴返回False
print()
# print("isubset()方法检测其是否是某个集合的子集")
print(s.issubset({2, 1, 3}))
print(s.issubset({4, 1, 3, 2}))
print(s.issubset({1, 2}))
print()
# print("isubset()方法检测其是否是某个集合的超集")
print(s.issuperset({2, 1, 3}))
print(s.issuperset({4, 1, 3, 2}))
print(s.issuperset({1, 2}))
print()
# print("union()方法把当前集合和某个任意集合构成并集")
a = {1, 2}
b = {3, 2}
print(a.union(b))
print()
# print("intersection()方法把当前集合和某个任意集合构成并集")
a = {1, 2}
b = {3, 2}
print(a.intersection(b))
print()
# print("difference()方法构成一个新的当前集合和某集合的差集")
a = {1, 2}
b = {3, 2}
print(a.difference(b))
# print("以上方法均可以多参数，不仅集合，还可以加入字符串等作为参数")
print()
# print("symmetric_difference()方法简单来说就是A∩B - A∪B，并把其所得的元素构成集合，称为对称差集")
a = {1, 2}
b = {3, 2}
print(a.symmetric_difference(b))
print()
# print("同时也可使用运算符直接进行判断")
print(a < {1, 2})  # 检测真子集
print('''检测运算符补充(除了<，=，>等):
'|'用于检测是否为并集
'&'用于检测是否为交集
'-'用于检测是否为差集
'^'用于检测是否为对称差集
使用运算符时，两边就只能是集合的类型了''')