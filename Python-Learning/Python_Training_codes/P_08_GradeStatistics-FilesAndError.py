with open("scores.txt", "w", encoding="UTF-8") as f:
    f.writelines(["85\n", "92\n", "\n", "abc\n", "78\n", "-5\n", "100"])
def parse_score(line):
    line = line.strip()
    if not line:
        return None
    try:
        value = int(line)
    except ValueError:
        raise ValueError(f"{line}, There are non-integers")
    if value < 0 or value > 100:
        raise ValueError(f"{line}, The score figures are illegal")
    return value
total = 0
invalid = 0
correct_times = 0
average = None
with open("scores.txt", "r", encoding="UTF-8") as d:
    for each in d:
        try:
            scores = parse_score(each)
        except ValueError as e:
            invalid += 1
        else:
            if scores is None:
                pass
            else:
                correct_times += 1
                total += scores
    if correct_times == 0:
        print("Invalid num")
    else:
        average = total / correct_times
        print("有效成绩: %d\n总分: %.2f\n平均分: %.2f\n无效行数: %d"%(correct_times, total, average, invalid))
# print('''问题总结:
# 1.for之后，每行的结果都是字符串，无法参与数的比较，需int一下
# 2.未用.strip方法清空空行的\\n，方便后续判断空行
# 3.忘做零除数保护了
# 4.遇到空行抛出的None也跟着进入运算了，需再条件判断一次
# 5.except ValueError接不住TypeError，所以line>100那个错误直接崩到顶层，没被主循环兜住
# 6.读写编码必须一致，写 UTF-8 就要读 UTF-8，不然中文文件必崩（纯英文只是侥幸）''')