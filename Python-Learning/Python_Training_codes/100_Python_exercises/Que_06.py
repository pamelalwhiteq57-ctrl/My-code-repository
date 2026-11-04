# Question:6
'''
利用递归算法，把输入的任意5个字符，以相反顺序打印出来
'''
def print_reverse(chars, idx = 0):
    if idx >= len(chars):
        return
    print_reverse(chars, idx + 1)
    print(chars[idx], end = "")
if __name__ == "__main__":
    data = input()
    print_reverse(data[:5])