import random as r
import time


game_elements=["Stone","Paper","Scissor"]
i=1

while i ==1:
    print("1:Stone \n2:Paper \n3:Scissor")
    user_choice = int(input("Enter your choice: "))

    computer_choice = r.randint(1,3)

    print("Thinking ")
    time.sleep(0.8)

    print("Computer selected",game_elements[computer_choice-1])

    if computer_choice == user_choice:
        print("This is a tie")

    elif (computer_choice==1 and user_choice==3) or (computer_choice==2 and computer_choice==1) or (computer_choice==3 and computer_choice==2):
        print("Computer Wins")

    else:
        print("You win")

    i =int(input("Type 1 to play again: "))




