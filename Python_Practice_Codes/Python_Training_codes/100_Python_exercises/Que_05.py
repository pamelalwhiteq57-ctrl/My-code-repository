# Question:5
'''
求 1+2!+3!+...+20! 的和
'''
total = 0
def factorials(num):
    if num <= 0:
        return 1
    else:
        return num * factorials(num - 1)
for each in range(1, 21):
    total += factorials(each)
print(total)