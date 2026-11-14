while True:
    score = int(input("Enter a score:"))
    level = ('D' if 0 <= score < 60 else
             'C' if 60 <= score < 80 else
             'B' if 80 <= score < 90 else
             'A' if 90 <= score <= 100 else
             'S' if score == 100 else
             'None')
    print("Your level is:", level)