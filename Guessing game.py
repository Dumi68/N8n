#Guessing game, we're guessing a number between 1 and 1000

import random


number_to_guess = random.randint(1, 1000)

while True:
    try:
        guess = int(input('Enter your guess (between 1 and 1000): '))
        if guess < number_to_guess:
            print('Too low! Try again.')
        elif guess > number_to_guess:
            print('Too high! Try again.')
        else:
            print(f'Congratulations! You guessed the number {number_to_guess} correctly!')
            break
    except ValueError:
        print('Awuva?!. Enter a number between 1 and 1000.') 
9