"""Program that loops until correct number is guessed"""

from random import randint

secret: int = randint(1, 10)
guess: int = int(input('Guess a number between 1 and 10: '))
number_of_tries: int = 0
max_tries: int = 3

while (guess != secret) and (number_of_tries < max_tries-1) :
    print("Wrong!")
    print("You have " + str(number_of_tries) + " tries left")
    if (guess < 1) or (guess > 10):
        
    if guess < secret:
        print('Too low!')
    else:
        print('Too high!')
        # if they were equal the loop will already have ended / that's why we don't need elif
    guess = int(input('Guess again: '))

    number_of_tries += 1

if guess == secret:
    print("Correct! The number is "+str(secret))
else:
    print("Too many tries")

