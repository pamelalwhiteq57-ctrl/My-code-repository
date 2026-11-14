"""Number Guessing Game"""

import random;

answer = random.randint(1, 10);

x = 3;

while x > 0:
    temp = input("Guess a number (1-10): ");
    guess = int(temp);

    if guess == answer:
        print("Guess right!");
        print("Good job!");
        break;
    else:
        if guess < answer:
            print("Guess too low!");
        else:
            print("Guess too high!");
        x = x - 1;
        if x == 2:
            print("2 remaining guesses");
        if x == 1:
            print("1 remaining guess");
        if x == 0:
            print("No more guesses!");

print("\nGame Over!");