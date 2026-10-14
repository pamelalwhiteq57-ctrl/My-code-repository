scores = [88, 45, 92, 67, 73, 55, 100, 81, 39, 76]
def analyze_scores(scores_list):
    pas = 0
    ave = float(sum(scores_list) / len(scores_list))
    scores_list.sort()
    max = scores_list[-1]
    for i in range(len(scores_list)):
        scores_list[i]
        if scores_list[i] >= 60:
            pas += 1
    return ave, max, pas
result = analyze_scores(scores)
print(f"平均分: {result[0]:.2f}\n最高分: {result[1]}\n及格人数: {result[2]}")
# print('''问题：
# 1.sort()方法修改了原列表
# 2.第8行是多余的，我们只需要pas的值即可
# 3.∵问题1，所以最大值无需使用sort()方法排序，只需使用max()函数即可
# 4.无空列表保护
# 移步Better文件查看修改后的结果''')