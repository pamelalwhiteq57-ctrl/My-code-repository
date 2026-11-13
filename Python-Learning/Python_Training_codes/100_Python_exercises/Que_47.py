# Question:47
'''
把一个字符串中由空格隔开的单词反序，同时反转每一个字符的大小写
例:
"Hello World"变形后为"wORLD hELLO"
'''
string = "Hello World"
def switch(s:str) -> str:
    temp_list = s.split(" ")
    res_str = " ".join(temp_list[::-1])
    return res_str.swapcase()
print(switch(string))