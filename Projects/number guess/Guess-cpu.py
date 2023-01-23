#Guess the number game from this tutorial: https://www.youtube.com/watch?v=8ext9G7xspg&t=100s

#Call a random number from python internally, using an integer between 1 and x
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low!')
        elif guess > random_number:
            print('Too high!')

#this loop breaks automatically because we used the does not equal function in the while loop.

    print(f'You got it! The number was {random_number}.')    

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct(C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer has guessed your {guess}')

#The number here is the upper limit of our X function
#guess(10) #change games here
computer_guess(10)