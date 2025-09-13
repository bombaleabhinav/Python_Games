import random as r
import time

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

print ("welcome!")
print(row1 /nrow2 /nrow3)
user_choice = int(input("Where do you want to place X: "))

def allot(input1,symbol):
    if input1 in row1:
        row1[user_choice-1]= symbol
    elif input1 in row3:
        row2[user_choice-4] = symbol
    else:
        row3[user_choice-7] = symbol

while i in range(5):
    user_choice = int(input("Where do you want to place X: "))
    allot(user_choice,"O")
    print("Computer Thinking")
    computer_choice= r.randint(1,9)
    allot(computer_choice,"X")





