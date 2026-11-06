# Question:9
'''
温度转换器：华氏度转摄氏度，转换公式：C = (F - 32) * 5/9
'''
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
x = float(input("请输入华氏度:"))
celsius = fahrenheit_to_celsius(x)
print("转化为摄氏度%.1f度"%(celsius))