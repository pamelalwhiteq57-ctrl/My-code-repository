scores = [88, 45, 92, 67, 73, 55, 100, 81, 39, 76]
def analyze_scores(scores_list):
    if not scores_list:
        return 0, 0, 0
    pas = 0
    ave = sum(scores_list) / len(scores_list)
    top = max(scores_list)
    for i in range(len(scores_list)):
        if scores_list[i] >= 60:
            pas += 1
    return ave, top, pas
average, highest, passs = analyze_scores(scores)
print(f"平均分: {average:.2f}\n最高分: {highest}\n及格人数: {passs}")
print(analyze_scores([]))