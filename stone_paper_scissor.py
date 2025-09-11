import random as r
import time


game_elements=["Stone","Paper","Scissor"]
i=0

while i ==0:
    print("1:Stone \n2:Paper \n3:Scissor")
    user_choice = int(input("Enter your choice: "))

    computer_choice = r.randint(1,3)

    if computer_choice == user_choice:
        print("This is a tie")

    elif (computer_choice==1 and user_choice==3) or (computer_choice==2 and computer_choice==1) or (computer_choice==3 and computer_choice==2):
        print("Computer Wins")

    else:
        print("You win")

