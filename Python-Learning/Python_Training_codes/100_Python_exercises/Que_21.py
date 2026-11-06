# Question:21
'''
找到年龄最大的人，并输出，例: person = {"li":18, "wang":50, "zhang":20, "sun":22}
'''
person = {"li":18, "wang":50, "zhang":20, "sun":22}
max_name = max(person, key = person.get)
print("年龄最大的是%s"%(max_name))