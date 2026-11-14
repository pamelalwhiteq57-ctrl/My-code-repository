def det2(m:list[list[int]]) -> int:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
def det3(m:list[list[int]]) -> int:
    return m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1] - m[0][2]*m[1][1]*m[2][0] - m[0][0]*m[1][2]*m[2][1] - m[0][1]*m[1][0]*m[2][2]
def submatrix(m:list, i:int, j:int) -> list:
    matrix = [each[:j] + each[j+1:] for each in m[:i] + m[i+1:]]
    return matrix
m3 = [[1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9]]
print(submatrix(m3, 0, 0))    # 期望 [[5, 6], [8, 9]]
print(submatrix(m3, 0, 1))    # 期望 [[4, 6], [7, 9]]
print(submatrix(m3, 1, 2))    # 期望 [[1, 2], [7, 8]]
print(submatrix(m3, 2, 2))    # 期望 [[1, 2], [4, 5]]
# print("以下为原列表是否修改对照")
before = [row[:] for row in m3]
submatrix(m3, 0, 0)
print("原矩阵没被改:", m3 == before)
print()
def det4(m):
    total = 0
    for j in range(4):
        sub = submatrix(m, 0, j)
        minor = det3(sub)
        coefficient = (-1) ** (1+(j+1))
        a = coefficient * minor
        total += m[0][j] * a
    return total