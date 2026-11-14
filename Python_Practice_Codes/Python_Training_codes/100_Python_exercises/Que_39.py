# Question:39
'''
字符串去重后排序
'''
def string_deduplicate_and_sort(s):
    unique_chars = sorted(set(s))
    return "".join(unique_chars)