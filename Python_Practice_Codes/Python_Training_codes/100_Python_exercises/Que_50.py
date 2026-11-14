# Question:50
'''
插入排序
通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
'''
def sequence(l:list) -> list:
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
data = [4, 6, 8, 5, 9]
sequence(data)
print(data)