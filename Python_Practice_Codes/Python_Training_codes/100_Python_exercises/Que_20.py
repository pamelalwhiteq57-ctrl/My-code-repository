# Question:20
'''
列表排序及连接
'''
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    a.sort()
    b.sort()
    print(a)
    print(b)

    print(a + b)

    a.extend(b)
    print(a)