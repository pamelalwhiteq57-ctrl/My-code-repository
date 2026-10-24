def fac(num):
    result = num
    for i in range(1, num):
            result *= i
    return result
print(fac(5))
print()
def factorial(num):
    if num <= 0:
         return 1
    else:
         return num * factorial(num-1)
print(factorial(5))