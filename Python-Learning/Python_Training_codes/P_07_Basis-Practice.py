print("1.")
time = int(input("Please enter a number:"))
h = time // 60
m = time % 60
print("%d hours, %d minutes"%(h, m))
print("2.")
score = int(input("Enter a score:"))
level = ('D' if 0 <= score < 60 else
         'C' if 60 <= score < 80 else
         'B' if 80 <= score < 90 else
         'A' if 90 <= score <= 100 else
         'None')
print("Your level is", level)
print("3.")
total = 0
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
print("4.")
maxnum = None
times = 0
while True:
    num = int(input("Please enter a number:"))
    if num == 0:
        break
    times += 1
    if maxnum is None or maxnum < num:
        maxnum = num
    sumtotal += num
print("times: %d, total: %d, max: %d"%(times, sumtotal, maxnum))
print()
n = int(input())
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()