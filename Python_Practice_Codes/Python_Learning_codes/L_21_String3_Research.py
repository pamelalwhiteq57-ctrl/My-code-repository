# print("字符串的查找，可选参数均为(sub[,start[,end]])")
# print("count用于统计子字符串在字符串中出现的次数")
x = "12040151"
print(x.count("1", 0, 4))
print()
# print("find用于查找子字符串在字符串中首次出现的下标索引，若不存在则返回-1")
# print("rfind用于倒序查找子字符串在字符串中首次出现的下标索引，若不存在则返回-1")
print(x.find("1", 1, 5))
print(x.rfind("1", 1, 6)) #左闭右开
# print("index用法与find类似，区别在于若不存在则会抛出异常，rindex同理")