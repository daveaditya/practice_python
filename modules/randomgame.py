from random import randint
import sys

number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        i = int(input(f'enter a number between {sys.argv[1]} and {sys.argv[2]}: '))

        if number == i:
            print('You guessed it right!')
            break
        else:
            print('Better luck next time. Let\'s try again.')
    except ValueError:
        print('please enter a number')
