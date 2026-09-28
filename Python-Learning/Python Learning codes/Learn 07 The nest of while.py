i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "*", i, "=", j * i, end=" ")
        j += 1
    print()
    i += 1

day = 1
hour = 1
while day <= 7:
    while hour <= 8:
        print("Today, I must insist on 8 hours!")
        hour += 1
        if hour > 1:
            break
    day += 1
#分析一下一共说了多少次“我要坚持8小时”？