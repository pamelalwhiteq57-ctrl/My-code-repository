s = [[0] * 3 for i in range(3)]
print(s)
print()
even = [i for i in range(10) if i % 2 == 0]
print(even)
print()
#改为[i+1 for i in range(10) if i % 2 == 0]
even1 = [i+1 for i in range(10) if i % 2 == 0]
print(even1)
#发现输出结果为原结果每个+1，说明程序先执行右边的if语句，再通过表达式赋值
#先执行for，再if，最后再执行左侧表达式
print()
words = ["inductive", "brew", "scandal", "intensive", "pendant"]
fwords = [w for w in words if w[0] == 'i']
print(fwords)
print()
#利用条件推导式找出以‘i’为首字母的word
#w[n],n必须<=列表中最小字符串的长度
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
flatten = [col for row in matrix for col in row]
print(flatten)
print()
#本质等于：
# for row in matrix:
#     for col in row:
#         flatten.append(col)
#即先外层通过in matrix锁定每一个内列表或字符串的索引，然后在内层循环中用那个值
#再次进行迭代，在选中的内列表中，输出每一个迭代后的col的值，然后再外层循环迭代
#例2:
k = [x + y for x in "Ewe" for y in "vdn"]
print(k)