import random
import hangman_words as hw


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
    print(hangman_logo)  # <-- actually print it

def print_life(lives):
    # Indexed by lives remaining: 6 (start) ... 0 (game over)
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


random_word = random.choice(hw.word_list)

lives = 6
found_word = ["_"] * len(random_word)
guessed = set()        # track all guesses
wrong_guesses = set()  # optional: track wrong guesses separately

print(" ".join(found_word))
print_life(lives)

while lives > 0:
    guess = input("Guess a letter: ").strip().lower()
    if not guess:
        print("Please enter a letter.")
        continue
    guess = guess[0]  # take first character only

    if guess in guessed:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    guessed.add(guess)
    indexes = [i for i, c in enumerate(random_word) if c == guess]

    if not indexes:
        wrong_guesses.add(guess)
        print(f"'{guess}' is not in the word. You lose a life.")
        lives -= 1
        print_life(lives)
    else:
        for i in indexes:
            found_word[i] = guess
        print("Nice! " + " ".join(found_word))

    print(f"Lives left: {lives}/6")
    if wrong_guesses:
        print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
    print("-" * 50)

    if "_" not in found_word:
        print("You win! The word was:", random_word)
        break

if lives == 0 and "_" in found_word:
    print("Game over! The word was:", random_word)
