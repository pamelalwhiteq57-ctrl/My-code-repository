rhyme = (1, 2, 3, 4, 5, "6789")
#类似于列表，可以用下标索引
print(rhyme[0])
print()
#支持切片操作
print(rhyme[:3])
print(rhyme[:])
print(rhyme[::2])
print(rhyme[::-1])
print()
#count和index这种查找型的也能使用
nums = (3, 1, 9, 6, 8, 3, 5, 3)
print(nums.count(3))
print(nums.index(9))
print()
#运算符能使用
x = (1, 2, 3)
y = (4, 5, 6)
print(x + y)
print(x * 3)
print()
#嵌套的元组和迭代
s = (1, 2, 3)
t = (4, 5, 6)
w = (s, t)
print(w)
print()
for i in w:
    for each in i:
        print(each)
print()
#∴仍然能使用列表推导
j = (1, 2, 3, 4, 5)
k = [each * 2 for each in j if each % 2 != 0]
print(k)
print()
#仅有一个元素的元组:
l = (1,)
print(l)
print(type(l))
print()
#解包：
m = (123, "option", 3.1415)
xx, yy, zz = m
print(xx, yy, zz)