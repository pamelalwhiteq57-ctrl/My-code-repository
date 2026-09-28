day = 1
while day <=7:
    answer = input("Have u done your homework today?(yes/no):")
    if answer != "yes":
        print("Oh no, u have not done your homework!")
        break
    day += 1
else:
    print("U have done your homework for 7 days in a row. Good job!")