import sys
from random import randint

# using sys to play random guessing game
# low_random = int(sys.argv[1])
# high_random = int(sys.argv[2])
# random_guess = int(sys.argv[3])

# dynamically asking user to input range and guess
low_random = int(input('What do you want the low value to be? '))
high_random = int(input('What do you want the high value to be? '))
while low_random > high_random:
    high_random = input(f'Please enter a number higher than {low_random} ')


def lets_play(guess, answer):
    if high_random >= answer >= low_random:
        if guess == answer:
            print('Nailed it!')
            return True
        if answer < answer:
            print('Guess higher')
        else:
            print('Guess lower')
    else:
        print(f'Hey bozo, I said between {low_random} and {high_random} ')
        return False


if __name__ == '__main__':
    random_answer = randint(int(low_random), int(high_random))
    while True:
        try:
            random_guess = int(input(f'Guess a number between {low_random} and {high_random} '))
            if lets_play(random_guess, random_answer):
                break
        except ValueError:
            print('Please enter a number')
            continue
