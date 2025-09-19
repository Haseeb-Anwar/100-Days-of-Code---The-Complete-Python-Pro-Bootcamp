import game_data as gd
import art
import random

winner=''
print(art.logo)

def play(item1,item2):
    print(f"\nCompare A: {item1['name']}: a {item1['description']} from {item1['country']} ({ item1['follower_count']} Followers)")
    print(art.vs)
    print(f"Compare B: {item2['name']}: a {item2['description']} from {item2['country']}:")


    if(item1['follower_count']>item2['follower_count']):
        return item1
    elif (item2['follower_count'] >= item1['follower_count']):
        return item2


    return  winner



item1=random.choice(gd.data)
item2=''
total_Score=0

for i in gd.data:
    item2 = random.choice(gd.data)


    winner=play(item1,item2)


    result=input("\nWho has more followers? Type 'A' or 'B': ")


    if(winner==item1):
        if(result=='A'):
            print(f"\nCorrect: {item1['name']} has more followers ({item1['follower_count']} Followers) ")
            total_Score+=1
            print(f"Your score is: {total_Score}")
        elif (result == 'B'):
            print(f"\nWRONG: {item1['name']} has more followers ({item1['follower_count']}  Followers) ")
            print(f"Your score is: {total_Score}")
            break

    if(winner==item2):
        if(result=='B'):
            print(f"\nCorrect: {item2['name']} has more followers ({item2['follower_count']}  Followers) ")
            total_Score += 1
            print(f"Your score is: {total_Score} ")
        elif (result == 'A'):
            print(f"\nWRONG: {item2['name']} has more followers ({item2['follower_count']} Followers) ")
            print(f"Your score is: {total_Score}")
            break




   # print(gd.data)