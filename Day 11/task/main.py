import art
import random
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


total_user=[]
total_dealer=[]

total_user.append(int(deal_card()))
total_user.append(int(deal_card()))
print("User First card:", total_user[0])
print("User Second card:", total_user[1])
print("User Total: ", sum(total_user))
print("---------------------------------------------")

total_dealer.append(int(deal_card()))
total_dealer.append(int(deal_card()))
print("Dealer First card:", total_user[0])
print("---------------------------------------------")
choice=input("Do you want to hit or stand?: h/s ")

while choice == "h":
    total_user.append(int(deal_card()))
    print("---------------------------------------------")
    print("User new card:",  total_user[-1])
    print("User Total: ", sum(total_user))
    print("---------------------------------------------")
    if sum(total_user)>21:
        print("Dealer wins!")
        break
    choice = input("Do you want to hit or stand?: h/s ")


print("Dealer Second card:", total_dealer[1])
print("Dealer Total: ", sum(total_dealer))
print("---------------------------------------------")


print("Total score user: ", sum(total_user))
print("Total score dealer: ",  sum(total_dealer))

if sum(total_user)>21:
    print("Dealer win!")
elif sum(total_dealer)>21:
    print("User win!")
else:
    if sum(total_dealer)>sum(total_user):
        print("Dealer win!")
    else:
        print("User win!")





