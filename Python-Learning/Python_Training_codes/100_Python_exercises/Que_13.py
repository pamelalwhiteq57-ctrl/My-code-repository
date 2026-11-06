# Question:13
'''
给一个不多余5位的正整数，呀要求:1.求它是几位数，2.逆序打印出各位数字
'''
def main():
    try:
        num = int(input("输入一个不超过5位的正整数:"))
    except ValueError as e:
        print(f"您输入的{e}不符合要求")
        return
    if num <= 0 or num > 99999:
        print("请输入 1~99999 之间的正整数")
        return
    num_str = str(num)
    print(f"该数是{len(num_str)}位数")
    print("逆序后为:", " ".join(reversed(num_str)))
if __name__ == "__main__":
    main()