# TODO-1: Import and print the logo from art.py when the program starts.

import art

print (art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=''
def encrypt(original_text,shift_amount):
    result = ""
    for char in original_text:
        if char.isalpha():  # only shift letters
            base = ord('A') if char.isupper() else ord('a')
            # shift by 2, wrap around using modulo 26
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # keep spaces, punctuation unchanged
    return result


def decrypt(text,shift_amount):
    result = ""
    for char in text:
        if char.isalpha():  # only shift letters
            base = ord('A') if char.isupper() else ord('a')
            # shift by 2, wrap around using modulo 26
            result += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            result += char  # keep spaces, punctuation unchanged
    return result



while direction!='quit':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, quit to close:\n").lower()

    if(direction=='encode'):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypted_text=encrypt(text,shift)
        print(encrypted_text)

    elif(direction=='decode'):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypted_text=decrypt(text,shift)
        print(decrypted_text)
    elif(direction=='quit'):
        break



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.




