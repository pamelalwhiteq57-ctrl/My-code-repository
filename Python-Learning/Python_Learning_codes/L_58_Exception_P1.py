try:
    # 可能出错的代码
    num = int(input("请输入一个数字："))
    result = 10 / num
    print(f"结果是：{result}")
except ZeroDivisionError:
    print("错误：不能除以零！")
except ValueError:
    print("错误：请输入有效的数字！")
print()
# print("as identifier可以提取异常原因")
try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
print()
# print("把多个异常使用元组的形式包裹起来")
try:
    1 / 0
    1 + "a"
except (ZeroDivisionError, ValueError, TypeError):
    pass    # 只要检测到了以上任何一个异常，都pass掉