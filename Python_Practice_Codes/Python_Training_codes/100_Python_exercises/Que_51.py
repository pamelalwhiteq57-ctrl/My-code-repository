# Question:51
'''
合并有序数组排序
'''
def merge_sorted(arr_a, arr_b):
    merged = []
    i, j = 0, 0
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] <= arr_b[j]:
            merged.append(arr_a[i])
            i += 1
        else:
            merged.append(arr_b[j])
            j += 1
    while i < len(arr_a):
        merged.append(arr_a[i])
        i += 1
    while j < len(arr_b):
        merged.append(arr_b[j])
        j += 1
    return merged
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print(merge_sorted(a, b))