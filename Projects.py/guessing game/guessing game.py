#this program is a number-guessing game. It will ask the user for their name and ask them to guess a number between 1 and 20. The participant will have a total of 7 attempts
import random
import sys
number = random.randint(1, 20)
print('Please type your name: ')
name = input()
# asks the user for name
print('hello ' + name + ', would you like to play a guessing game? y/n')
decision = input()
# program terminates if the input is 'n' and proceeds if it is 'y' or 'Y'
if decision == 'Y' or 'y':
    print('lets proceed')
elif decision == 'n' or 'N':
    print('Goodbye')
    sys.exit()
print('You have a maximum of 7 attempts.')
# returns the user to 'Guess a number when a certain input is entered
while True:
    for guessesNum in range(7):
        print('Guess a number between 1 and 20')
        guess = int(input())
        if guess < number:
            print('Go higher')
        elif guess > number:
            print('Go lower')
        else:
            break
    if guess == number:
        print('Great job, you guessed the right number in ' +
              str(guessesNum) + ' attempt(s)')
    else:
        print('The correct number is ' + str(number))
    print('Would you like to play again? y/n')
    playAgain = input()
# asks user to decide if they want to play again
    if playAgain == 'Y' or 'y':
        break
    elif playAgain == 'N' or 'n':
        sys.exit()
