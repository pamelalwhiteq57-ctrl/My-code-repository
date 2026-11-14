# Question:29
'''
现有两个列表，fruit和number，把这两个列表组成字典，然后在字典中输入水果品种查询该水果的数量
如输入不属于字典中的水果，则输出0
'''
fruit = ['apple', 'banana', 'strawberry', 'orange', 'mango', 'grape', 'blueberry']
number = [1, 3, 5, 6, 13, 21, 10]

inventory = dict(zip(fruit, number))
x = input("输入你想查询的水果名:")
# inventory.get(x, print("未存在此种类"))
try:
    print(inventory[x])
except KeyError:
    print(0)