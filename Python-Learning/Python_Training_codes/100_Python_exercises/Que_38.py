# Question:38
'''
去除字符串中重复的字符，保持原有排序
'''
def remove_duplicates(s):
    seen = set()
    res = []
    for char in s:
        if char in seen:
            continue
        seen.add(char)
        res.append(char)
    return "".join(res)
string = "111112345556"
print(remove_duplicates(string))