# Random number guessing game

import random

guessTaken = 0

print("Hello what's your name?")
userName = input()

number = random.randint(1, 100)
print("Hi " + userName + " nice to meet you")

print("Guess a number between 1 - 100.")

while guessTaken < 6:
    print("Take a guess")
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print("Higher!")

    if guess > number:
        print("Lower!")

    if guess == number:
        break

if guess == number:
    print("Great! You got it in " + str(guessTaken) + " tries!")

if guess != number:
    print("Wow, you lost. The number was " + str(number) + " !")
