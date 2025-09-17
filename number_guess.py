import random
import time

print("The computer chooses a random number bettween 0 and 1000")
time.sleep(0.5)
print("You have 5 tries")
time.sleep(0.5)
print("Good Luck!")

computer_guess = random.randint(0,1000)
user_guess = int(input("Enter your first guess: "))


for i in range(7):
    if user_guess==computer_guess:
        print("You Win")
        time.sleep(0.5)
    else:
        if user_guess>computer_guess:
            print("Lower! ")
        else:
            print("Higher! ")
        user_guess= int(input("Enter your next guess: "))

if user_guess==computer_guess:
    print("You win! ")

else:
    print("You are a Loser! ")

