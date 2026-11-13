# Question:40
'''
切片取出列表中最大的三个数
'''
numbers = [3, 1, 4, 1 ,5, 9, 2, 6, 5, 3, 5]
largest_three = sorted(numbers, reverse=True)[:3]
print(largest_three)