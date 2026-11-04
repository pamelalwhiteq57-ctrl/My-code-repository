# Question:3
'''
输入三个整数x，y，z，把这三个数由小到大输出
'''
x = int(input("请输入第一个整数:"))
y = int(input("请输入第二个整数:"))
z = int(input("请输入第三个整数:"))
nums = [x, y, z]
nums.sort()
print("从小到大分别是: %d, %d, %d"%(nums[0], nums[1], nums[2]))