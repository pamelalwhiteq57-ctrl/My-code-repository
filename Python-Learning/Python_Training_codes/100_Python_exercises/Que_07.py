# Question:7
'''
判断一个输入的五位数是否是回文数，即个位数等于万位数，十位数等于千位数
'''
def func(num):
    return (
        num.isdigit()
        and num[0] != '0'
        and len(num) == 5
        and num == num[::-1]
    )
value = input("请输入一个五位数:")
if func(value):
    print("是回文数")
else:
    print("不是回文数")