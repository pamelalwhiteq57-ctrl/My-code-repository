try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在！")
else:          # 未检测到异常执行的内容
    print("读取成功，内容长度：", len(content))
finally:       # 必定执行的内容5
    print("无论是否出错，这里都会执行")
print()
# print("快速捕获多种异常,Exception是一个异常基类,可以捕获其自己和其子类异常")
try:
    # 1 / 0
    # "a" + 1
    a = [1]
    a[6]
except Exception as e:
    print(e)
print()
# print("raise语句，用于主动抛出异常")
def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age
try:
    set_age(-5)
except ValueError as e:
    print(f"捕获到错误：{e}")
print()
# print("assert语句只引发AssertionError的异常，多用于调试")
a = []
def average(nums):
    assert nums, "列表不能为空"
    return sum(nums) / len(nums)
print(average(a))