# Question:30
'''
输入一个字符串s，只包含大小写英文字母
输出每个字符及其出现次数，用空格间隔，每个字母单独一行
'''
s = input("输入单词:")
seen = set()
if not (s.isalpha() and s.isascii()):
    exit()
for each in s:
    if each in seen:
        continue
    seen.add(each)
    print("%s %d" % (each, s.count(each)))