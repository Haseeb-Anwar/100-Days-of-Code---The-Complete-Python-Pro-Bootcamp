
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


pw_list = [""] * (nr_letters + nr_symbols + nr_numbers)


for i in range(nr_letters):
    random_value = random.choice(letters)
    valid_indexes = [i for i, v in enumerate(pw_list) if v == ""]
    random_index = random.choice(valid_indexes)
    pw_list[random_index]=random_value;



for i in range(nr_symbols):
    random_value = random.choice(symbols)
    valid_indexes = [i for i, v in enumerate(pw_list) if v == ""]
    random_index = random.choice(valid_indexes)
    pw_list[random_index]=random_value;



for i in range(nr_numbers):
    random_value = random.choice(numbers)
    valid_indexes = [i for i, v in enumerate(pw_list) if v == ""]
    random_index = random.choice(valid_indexes)
    pw_list[random_index]=random_value



result = "".join(pw_list)
print(f"Your password is: {result}")




## The solution file has better approach





