# Question:27
'''
输入一个正整数，如果是素数，输出YES，否则输出NO
'''

num = int(input("输入正整数:"))
if num <= 0:
    print("请输入正整数")
else:
    def is_prime(n) -> bool:
        if n == 1: return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    if is_prime(num):
        print("YES")
    else:
        print("NO")