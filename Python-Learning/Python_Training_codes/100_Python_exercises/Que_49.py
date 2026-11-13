# Question:49
'''
选择排序
设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素并找到最小元素，记录最小元素下标，和第0个下标
元素进行交换
'''
test = [6, 3, 5, 7, 0]
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
print(test)
selection_sort(test)
print(test)