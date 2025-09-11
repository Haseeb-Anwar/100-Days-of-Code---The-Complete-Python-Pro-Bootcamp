import random

def print_hangman():
    hangman_logo = r"""
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    """



def print_life(lives):
    hangman_stages = [
        # 0 lives left (game over)
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """,
        # 1 life left
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        # 2 lives left
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        # 3 lives left
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        # 4 lives left
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        # 5 lives left
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        # 6 lives left (start)
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """
    ]

    print(hangman_stages[lives])



print_hangman()

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)

life_counter=6
guess_a_letter=''
found_word=list(random_word)
found_word = ["_"] * len(found_word)

#print(random_word)
print (found_word)





while life_counter>0:
    print(" ".join(found_word))
    guess_a_letter = input("Guess a letter: ")



    indexes = [i for i, c in enumerate(random_word) if c == guess_a_letter]


    if not indexes:

        print(f"you guessed: {guess_a_letter}, that's not in a word. you loose a life" )
        life_counter-=1
        print(f'life counter: {life_counter}')
        print(print_life(life_counter))

    else:

        for i in indexes:
            found_word[i]=guess_a_letter


        print(" ".join(found_word))

    print(f"***********************************{life_counter}/6 lives left *****************************************")









# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.





# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.



