import random as r
import time

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

print ("welcome!")
print("\n",row1,"\n",row2,"\n",row3)
user_choice = int(input("Where do you want to place X: "))
computer_choice= r.randint(1,9)
    

for i in range(5):
    user_choice = int(input("Where do you want to place X: "))

    if user_choice in row1:
      row1[user_choice-1]= "O"
    elif input1 in row3:
      row2[user_choice-4] = "O"
    else:
     row3[user_choice-7] = "O"

     print("Computer Thinking")
     

    if computer_choice in row1:
        row1[computer_choice-1]= "O"
    elif input1 in row3:
        row2[computer_choice-4] = "O"
    else:
        row3[computer_choice-7] = "O"

    print(row1,"\n",row2,"\n",row3)





