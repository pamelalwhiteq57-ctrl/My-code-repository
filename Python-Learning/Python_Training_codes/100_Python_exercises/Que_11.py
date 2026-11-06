# Question:11
'''
利用递归求5!
'''
def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))