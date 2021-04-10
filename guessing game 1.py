import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Enter a guess between 1 and {x}:'))
        if guess<random_number:
            print('sorry, try again guess too low')
        elif guess>random_number:
            print('sorry try again guess too high')
        else:
            print(f'you guessed the number {random_number} correctly')

guess(10)