print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age=int(input("What is your Age?:"))

    if age<12:
        print("Ticket is $5")
    elif age <=18:
        print("Ticket is $7")
    else:
        print("Ticket is $12")

else:
    print("Sorry you have to grow taller before you can ride.")
