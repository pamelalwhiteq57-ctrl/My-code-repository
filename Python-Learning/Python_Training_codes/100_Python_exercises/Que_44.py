# Question:44
'''
猜数字游戏，生成一个1到100的随机数，玩家猜中就终止
'''
import random

secret = random.randint(1, 100)
count = 0

while True:
    try:
        guess = int(input("猜一个 1~100 的数:"))
    except ValueError:
        print("请输入数字")
        continue
    count += 1
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print(f"猜对了！答案是 {secret}，你一共猜了 {count} 次")
        break