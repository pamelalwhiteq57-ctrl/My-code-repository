# Question:26
'''
A正在背九九乘法表，现输入一个数n，打印九九乘法表中的1~n行
输入一个整数n，1 <= n <= 9
'''
def main():
    try:
        n = int(input().strip())
    except Exception:
        return
    for i in range(1, n + 1):
        line_parts = []
        for j in range(1, i + 1):
            line_parts.append(f"{i}*{j}={i * j}")
        print(" ".join(line_parts))
if __name__ == "__main__":
    main()