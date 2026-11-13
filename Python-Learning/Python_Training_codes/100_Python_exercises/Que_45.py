# Question:45
'''
最长公共前缀
给你一个大小为n的字符串数组strs,其中包含n个字符串,编写一个函数来查找字符串数组中的最长公共前缀,并返回
输入描述:["abca", "abc", "abca", "abc", "abcc"]
输出描述:"abc"
'''
strs = ["abca", "abc", "abca", "abc", "abcc"]
def longest_common_prefix(s):
    if not s:
        return ""
    prefix = min(s, key = len)
    for i in range(len(s)):
        while not s[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
print(longest_common_prefix(strs))