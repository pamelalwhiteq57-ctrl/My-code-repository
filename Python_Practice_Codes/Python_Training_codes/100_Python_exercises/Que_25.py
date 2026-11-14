# Question:25
'''
A和B一起玩密码游戏，A作为发送方会发送一个4位数的整数给B，B接收后将对密码进行破解。破解方案如下:
每位数字都要加上3再除以9的余数代替该位数字，然后将第1位和第3位数字交换，第2位和第4位数字交换
求B破解出的代码
'''
original_password = input("输入原密码:")
if not original_password.isdigit():
    print("请输入数字密码")
    exit()
def decrypt_password(num_str:str) -> str:
    if len(num_str) != 4:
        print("请输入合理位数的密码")
        return
    else:
        templist = []
        password = num_str
        for each in password:
            x = int(each)
            num = str((x + 3) % 9)
            templist.append(num)
        result = "".join(templist)
        final = result[2] + result[3] + result[0] + result[1]
        print(final)
        return
decrypt_password(original_password)