# print('''enumerate()函数的作用
# 返回一个枚举对象，将可迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表，且序号总在前''')
seasons = ["Spring", "Summer", "Autumn", "Winter"]
enumerate(seasons)  # 获得一个seasons的枚举对象
a = list(enumerate(seasons))  # 把它转化为列表
print(a)
# print("可通过start参数修改序号开始的值，默认0")
b = list(enumerate(seasons, 9))
print(b)
c = ['a', 'b', 'c', 'd']
for index, value in enumerate(c):
    print(f"下标值是{index}，值是{value}")
print()
# print('''zip()函数的作用
# 创建一个聚合多个可迭代对象的迭代器
# 把作为参数传入的每个可迭代对象的每个元素依次对应组合成元组''')
x = [1, 2, 3]
y = (4, 5, 6)
zippe = zip(x, y)
print(list(zippe))
z = "78910"
zipped = zip(x, y, z)
print(list(zipped))
# print("若不想抛弃作为参数的可迭代对象中多余的元素，则可以:")
import itertools
zippedd = itertools.zip_longest(x, y, z)
print(list(zippedd))
print()
# print("map()函数，会根据提供的函数，对指定的可迭代对象的每个元素进行运算，并返回最终结果的迭代器")
mapped1 = map(ord, "EWEVDN")
print(list(mapped1))  # ord是对每个字符进行Unicode求值
mapped2 = map(pow, [1, 2, 3], [4, 5, 6])
print(list(mapped2))  # pow是进行次方运算，前后的可迭代对象中的元素中一一对应,前者的元素作为底数，后者的元素总作为次数
# print("pow()中前后长度不一致时，处理方法与zip()类似，忽略多出来的")
print(list(map(max, [1, 3, 5], [2, 2, 2], [0, 3, 9, 8])))  #选出最大的组成迭代器，多的那个忽略(抛弃)
print()
# print("filter()函数，与map()类似，先是一个函数(规则)，并进行运算看是否符合，在运算完成后，返回最终计算结果为True的元素的迭代器")
print(list(filter(str.islower, "eWEvDn")))