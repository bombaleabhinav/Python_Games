import random
import time

print("The computer chooses a random number bettween 0 and 1000")
time.sleep(0.5)
print("You have 5 tries")
time.sleep(0.5)
print("Good Luck!")

computer_guess = random.randint(0,1000)
user__guess = int(input("Enter your firs guess: "))


while computer_guess==