# Question:31
'''
现有列表[3, 6, 9, 0, 5, 8]，请将其转化为元组，然后输出该元组后半部分。
再输入数字n，判断n是否在元组中，若不在，则将其复制三份后添加到元组末尾，最后输出最终元组长度
'''
base_list = [3, 6, 9, 0, 5, 8]
base_tuple = tuple(base_list)
res = base_tuple[len(base_tuple) // 2:] # 原使用列表推导式，发现切片更简单
for i in res:
    print(i)

n = int(input("输入整数:"))
if n in base_tuple:
    print(f"其在此元组中\n最终元组长度为{len(base_list)}")
else:
    temp = (n, n, n)
    new = base_tuple + temp
    print(f"最终元组为{new}\n最终元组长度为{len(new)}")