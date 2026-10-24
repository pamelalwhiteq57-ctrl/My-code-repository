scores = [88, 45, 92, 67, 73]
config = {"pass_line": 70}
def make_report(*args, **kwargs):
    pas = 0
    if not args:
        return 0, 0, 0, 0
    num = len(args)
    ave = sum(args) / len(args)
    top = max(args)
    pass_line = kwargs.get("pass_line", 60)
    for i in args:
        if i >= pass_line:
            pas += 1
    return num, ave, top, pas
all_people, average, highest, over = make_report(*scores, **config)
print(f"人数: {all_people} | 平均分: {average:.2f} | 最高分: {highest} | 及格人数: {over}")
# print('''错误点:
# 1.第15行的kwargs(原为kwargs=config)，未解包config就传入了，使得pass_line无法成为关键字参数并起作用
# 2.第15行在函数中，整个值都是config，关键字参数kwargs是键，所以第10行不能正常生效
# 3.解包后，原字典的键值对才能作为函数中的键值对使用''')