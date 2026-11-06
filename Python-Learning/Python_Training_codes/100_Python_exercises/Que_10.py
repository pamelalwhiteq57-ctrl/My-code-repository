# Question:10
'''
闰年判断器，1.能被4整除但不能被100整除，2.或者能被400整除
'''
def  is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
try:
    years = int(input("输入一个年份:"))
    if is_leap_year(years):
        print("%d年是闰年"%(years))
    else:
        print("%d年是平年"%(years))
except ValueError as e:
    print(f"{e}不是有效年份")