import random

number = random.randint(1, 20)

guesses = 0

while guesses < 3:
    guess = input("what is the number?")
    guess = int(guess)
    guesses = guesses + 1
    if guess > number:
        print("sorry, your number is too high. Try again.")
    if guess < number:
        print("sorry, your number is too low. Try again. ")
    if guess == number:
        break
if guess == number:
    print("You have selected the correct number.")
if guess != number:
    print("You have lost. The correct number is {}").format(number)
