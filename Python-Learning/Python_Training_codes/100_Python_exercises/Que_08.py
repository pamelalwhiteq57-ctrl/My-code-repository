# Question:8
'''
利用运算符的嵌套来完成，成绩>=90的用A表示，60~89分之间的用B表示，60分以下的用C表示
'''
score = float(input("请输入分数:"))
grade = 'A' if score >= 90 else ('B' if score >= 60 else 'C')
print(f"成绩{score}分对应的等级是:{grade}")