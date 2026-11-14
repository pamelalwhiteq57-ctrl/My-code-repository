# Question:37
'''
输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1,从0开始计数
'''
def check(A:str, B:str) -> int:
    res = B.find(A)
    return res
a = "4"
b = "12345"
print(check(a, b))