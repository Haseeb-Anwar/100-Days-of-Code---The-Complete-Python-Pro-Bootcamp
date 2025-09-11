
import my_module

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''





my_choice=input("Enter your choice (Rock/Paper/Scissor) :")



print("Your choice is: "+my_choice)

if my_choice=="Rock":
    print(rock)
if my_choice=="Scissor":
    print(scissors)
if my_choice=="Paper":
    print(paper)



computer_choice=my_module.play_rpc()

Result =""

print("Computer's choice is: "+computer_choice)

if computer_choice=="Rock":
    print(rock)
if computer_choice=="Scissor":
    print(scissors)
if computer_choice=="Paper":
    print(paper)




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