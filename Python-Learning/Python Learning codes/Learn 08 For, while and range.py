print("="*40)
print("1. for循环的使用")
print("="*40)
for each in "123456789":
    print(each,end=" ")
print("\n")
#上下两组代码块效果是相同的

print("="*40)
print("2. while循环与其相同结果的使用")
print("="*40)
i = 0
while i < len("123456789"):
    print("123456789"[i],end=" ")
    i += 1
print("\n")

#range()函数的使用
print("="*40)
print("3. range()函数的使用(1 to 10)")
print("="*40)
for j in range(1, 10):
    print(j,end=" ")
print("\n")
#这是从1到10，不包括10，若是range(10),则是从0到10但不包括10

print("="*40)
print("4. range()函数的使用(1 to 10,步进为2)")
print("="*40)
for k in range(1, 10, 2):
    print(k,end=" ")
print("\n")
#发现，这是从1到10，其步进为2，即每次加2,其也可为负数

print("="*40)
print("5. range()函数的使用(从1加到1E6)")
print("="*40)
sum = 0
for m in range(1, 1000001):
    sum += m
print(f"1到1E6的和为:{sum}")
#利用for计算1到1E6的和