#incorporate the random library
import random

#Print title
print("Let's play (R)ock (P)aper (S)cisor!")

#specify the three options
options = ["r", "p", "s"]

#computer selection
computer_choice = random.choice(options)

#user selection
user_choice = input("Make your choice: ")
print("Computer choosed: " + computer_choice)
if (computer_choice == user_choice):
    print("It's a draw")
elif (computer_choice == "r" and user_choice == "s") or (computer_choice == "s" and user_choice == "p"):
    print("Computer wins")
else:
    print("User wins")
