import my_module


my_choice=input("Enter your choice (Rock/Paper/Scissor) :")

print("Your choice is: "+my_choice)

computer_choice=my_module.play_rpc()

Result =""

print("Computer's choice is: "+computer_choice)


if my_choice==computer_choice:
    Result='Tie - No winner'

if my_choice=="Rock" and computer_choice=="Paper":
    Result="Computer Wins"

if my_choice=="Rock" and computer_choice=="Scissor":
    Result="You Win"

if my_choice == "Paper" and computer_choice == "Rock":
    Result = "Computer Wins"

if my_choice == "Paper" and computer_choice == "Scissor":
    Result = "You Win"

if my_choice == "Scissor" and computer_choice == "Rock":
    Result = "Computer Wins"

if my_choice == "Scissor" and computer_choice == "Paper":
    Result = "You Win"


print("The Result is: "+Result)