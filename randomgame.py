import sys
from random import randint

# using sys to play random guessing game
low_random = int(sys.argv[1])
high_random = int(sys.argv[2])

# dynamically asking user to input range and guess
# random_guess = int(sys.argv[3])
# low_random = int(input('What do you want the low value to be? '))
# high_random = int(input('What do you want the high value to be? '))

while low_random > high_random:
    high_random = input(f'Please enter a number higher than {low_random} ')

random_answer = randint(int(low_random), int(high_random))


while True:
    try:
        random_guess = int(input(f'Guess a number between {low_random} and {high_random} '))
        if high_random > random_guess > low_random:
            if random_guess == random_answer:
                print('Nailed it!')
                break
            if random_guess < random_answer:
                print('Guess higher')
            else:
                print('Guess lower')
        else:
            print(f'Hey bozo, I said between {low_random} and {high_random} ')
    except ValueError:
        print('Please enter a number')
        continue
