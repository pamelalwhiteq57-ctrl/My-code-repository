# oho = [1, 2, 3, 4, 5, 6]
# for i in range(len(oho)):
#     oho[i] = oho[i] * 2
# print(oho)
print()
#使用列表推导式得到相同结果：
olo = [1, 2, 3, 4, 5, 6]
olo = [i * 2 for i in olo]
print(olo)
print()
#使用列表推导式处理矩阵：(获取列co2和主对角线diag)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
col2 = [row[1] for row in matrix]
print(col2)
diag = [matrix[i][i] for i in range(len(matrix))]
print(diag)
fdiag = [matrix[j][2-j] for j in range(len(matrix))]
print(fdiag)