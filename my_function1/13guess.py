from random import randint

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    target = randint(1, 20)
    guesses = 0

    while True:
        num = int(input("Take a guess.\n"))
        guesses += 1


        if num < target:
            print("Your guess is too low.\n")

        elif num > target:
            print("Your guess is too high.\n")

        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
