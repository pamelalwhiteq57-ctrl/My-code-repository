# Question:18
'''
求输入数字的平方，如果平方运算小于50则退出
'''
def calc_square_loop() -> None:
    while True:
        num = input("输入任意数:")
        if not num.strip():
            print("输入为空，请重新输入")
        try:
            num1 = float(num)
            result = num1 ** 2
            if result < 50:
                break
            else:
                return "结果为:%.2f"%(result)
        except ValueError as e:
            print(f"{e}不是一个有效数字")

calc_square_loop()