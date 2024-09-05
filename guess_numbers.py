import random

top_of_range = input("Type the number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("type the number greater than 0")
        quit()
    else:
        random_number = random.randint(0,top_of_range)
    guess=0
    while True:
        guess+=1
        guess_number=input("guess the number: ")
        if guess_number.isdigit():
            guess_number = int(guess_number)
        else:
            print("Please type a number.")
            continue

        if guess_number == random_number:
            print("u got it ")
            break
        elif guess_number > random_number:
            print("u are above the number")
        else:
            print("you are below the number")
else:
    print("write the numbers for the game")
    quit()

print("you have ", guess, "guess")