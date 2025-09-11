
import random


def play_rpc():

    random_rock_paper_scissor = random.randint(0, 2)
    if random_rock_paper_scissor == 0:
        return("Rock")

    elif  random_rock_paper_scissor==1:
        return("Paper")

    else:
     return("Scissor")

