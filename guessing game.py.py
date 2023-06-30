import random
number = random.randint(1, 20)
print('Please type your name: ')
name = input()
print('hello ' + name + ', would you like to play a guessing game? y/n')
decision = input()
if decision == 'Y' or 'y':
    print('lets proceed')
elif decision == 'n':
    print('Goodbye')
while True:
    for guessesNum in range(1, 7):
        print('Guess a number')
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
    if playAgain == 'Y' or 'y':
        continue
    elif playAgain == 'n' or 'N':
        break
