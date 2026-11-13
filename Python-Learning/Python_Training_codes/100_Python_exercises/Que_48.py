# Question:48
'''
字符串压缩法，利用重复出现的次数
例:"aabcccccaaa" -> "a2bc5a3"
''' 
test_str = "aabcccccaaa"
# def compress_string(s:str) -> str:
#     counts = 1
#     temp_list = []
#     for i in range(len(s)):
#             try:
#                 if s[i] != s[i + 1]:
#                     temp_list.append(s[i])
#                     temp_list.append(str(counts))
#                     counts = 1
#                 else:
#                     counts += 1
#             except IndexError:
#                 temp_list.append(s[i])
#                 temp_list.append(str(counts))
#                 return "".join(temp_list)
# print(compress_string(test_str))

def compress_string(s: str) -> str:
    if not s:
        return ""
    result = []
    current = s[0]         
    count = 1
    for ch in s[1:]:       
        if ch == current:
            count += 1     
        else:
            result.append(current + (str(count) if count > 1 else ""))
            current = ch
            count = 1
    result.append(current + (str(count) if count > 1 else ""))
    return "".join(result)
print(compress_string(test_str))