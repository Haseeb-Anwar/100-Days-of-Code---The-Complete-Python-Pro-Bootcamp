import random
import art

print(art.logo)


difficulty= input("Choose difficulty? easy/hard: ")
attempts=0
num=random.randint(1, 100)

if difficulty=='easy':
    attempts=10

elif difficulty=='hard':
    attempts=5


for i in range(0,attempts-1):
    guess = int(input("Guess the number: "))
    if(guess>num):
        print ("Too High!")
    if (guess < num):
        print("Too Low!")
    if (guess == num):
        print("Hurrayy you won!!!")
        break
    if(i==attempts):
        print("Out of attempts... Try Again")
    print(f"{attempts-i} Attempts left!!!" )

