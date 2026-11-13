# Question:46
'''
判断一个字符串中每个字符是否全不同
'''
def evaluate(s):
    return len(set(s)) == len(s)
t1 = "qwertyuiop"
t2 = "qqertyuiop"
print(evaluate(t1))
print(evaluate(t2))