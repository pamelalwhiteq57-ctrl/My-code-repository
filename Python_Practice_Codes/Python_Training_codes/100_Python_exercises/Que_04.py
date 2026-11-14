# Question:4
'''
输入一串字符，分别统计出其中英文字母，空格，数字以及其他字符的个数
'''
alpha = 0
space = 0
decimal = 0
another = 0
string = input("请输入一行任意字符:")
for each in string:
    if each.isspace():
        space += 1
    elif each.isdecimal():
        decimal += 1
    elif each.isalpha() and each.isascii():
        alpha += 1
    else:
        another += 1
print(f"字母个数为:{alpha}\n空格个数为:{space}\n数字个数为:{decimal}\n其他字符个数为:{another}")