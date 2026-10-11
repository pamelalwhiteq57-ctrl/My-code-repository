# print('''
# keys()方法创建键的视图对象
# values()方法创建值的视图对象
# items()方法创建键值对的试图对象''')
a = dict.fromkeys("ABCDE", 0)
print(a.keys())
print(a.values())
print(a.items())
print()
# print("视图对象:原字典发生改变时，跟着改变")
a.pop("E")
print(a.keys())
print(a.values())
print(a.items())