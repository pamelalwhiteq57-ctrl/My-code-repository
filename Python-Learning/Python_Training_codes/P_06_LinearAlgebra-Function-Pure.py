def det3(m:list[list[int]]) -> int:
    return m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1] - m[0][2]*m[1][1]*m[2][0] - m[0][0]*m[1][2]*m[2][1] - m[0][1]*m[1][0]*m[2][2]
def submatrix(m:list, i:int, j:int) -> list:
    matrix = [each[:j] + each[j+1:] for each in m[:i] + m[i+1:]]
    return matrix
def det4(m:list[list[int]]) -> int:
    total = 0
    for j in range(4):
        sub = submatrix(m, 0, j)
        minor = det3(sub)
        coefficient = (-1) ** (1+(j+1))
        a = coefficient * minor
        total += m[0][j] * a
    return total
print()
x = [[1, 0, 2, 0], 
     [0, 2, 2, 3], 
     [3, 0, 4, 0], 
     [0, 4, 0, 1]]
print(det4(x))