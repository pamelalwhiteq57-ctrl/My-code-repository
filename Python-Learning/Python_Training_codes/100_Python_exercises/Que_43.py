# Question:43
'''
浅复制列表
'''
# 法一:
list1 = [1, 2, 3, 4, 5]
copy_list1 = list1[:]

# 法二:
list2 = [1, 2, 3, 4, 5]
copy_list2 = list(list2)

# 法三:
list3 = [1, 2 ,3 ,4, 5]
copy_list3 = list3.copy()