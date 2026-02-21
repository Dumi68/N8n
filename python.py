import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled a {die1} and a {die2}. Total: {die1 + die2}')
    elif choice == 'n':
        print('Mojo, hamba!')
        break
    else:
        print('Ndithi bhala u "y" or "n" wena ubhala ubhontsi. Please enter "y" or "n".')
    
