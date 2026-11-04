class C:
    def __getitem__(self, index):
        return index
c: C = C()
print(c[2])  # 对象进行索引操作时拦截
print()
class D:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
d: D = D([1, 2, 3, 4, 5])
print(d[1])  # 使用索引访问元素
d[1] = 5  # 使用索引修改元素
print(d[1])  # 输出修改后的元素
d[2:4] = [2, 3] # 使用切片修改元素
print(d.data)  # 输出修改后的列表6...