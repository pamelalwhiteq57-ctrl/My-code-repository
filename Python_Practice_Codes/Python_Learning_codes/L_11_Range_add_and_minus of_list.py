name = [1, 2, 3, 4, 5, "12345"]
print(name[2:4])
print(name[:2])
print(name[2:])
#列表切片的范围解析，即：左闭右开
print()
print()
x = [1, 2, 3, 4]
x.append(5)
#添加单个元素用append
print(x)
print()
print()
y = [1, 3, 4]
y.extend([5, 6, 7, 8])
print(y)
#添加一组元素用extend
print()
print()
z = [1, 3, 4, 5, 6]
z.insert(1,2)
print(z)
#在指定位置插入元素用insert,如insert(m,n),m为所需位置的索引，n为元素
print()
print()
s = [0,1,1,2,3,4]
s.remove(1)
print(s)
#remove(k)，k为指定元素本身，若存在多个相同的，则只删除第一个
print()
print()
f = [0,1,2,2,3,4]
f.pop(2)
print(f)
#删除指定位置元素，pop
#删除全部元素为clear()，如name.clear(),那么print(name)的结果为[],即空列表