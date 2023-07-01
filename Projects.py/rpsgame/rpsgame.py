#This is a rock paper and scissors game. It follows the official rules of rock paper and scissors, the number of times one can play is unlimited at the moment
import random, sys
Win= 0
Loss= 0
Tie= 0
print('ROCK, PAPER, SCISSORS')
while True:
  print('%s Wins,%s Losses,%s Ties' %(Win, Loss, Tie))
  while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove= input()
    if playerMove == 'q':
      sys.exit()
    elif playerMove== 'r' or playerMove=='p' or playerMove=='s':
      break
    print("please type one of r, p, s or q.")

  if playerMove == 'r':
    print('ROCK versus...')
  if playerMove =='p':
    print('PAPER versus...')
  if playerMove =='s':
    print('SCISSORS versus...')

  randomNumber = random.randint(1,3)

  if randomNumber== 1:
    computerMove='r'
    print('ROCK')
  elif randomNumber==2:
    computerMove='p'
    print('PAPER')
  elif randomNumber==3:
    computerMove='s'
    print('SCISSORS')
  if playerMove == computerMove:
    print('It is a tie!')
    Tie= Tie +1
  elif playerMove =='r' and computerMove=='p':
    print('You lost!')
    Loss= Loss +1
  elif playerMove =='r' and computerMove=="s":
    print('You won!')
    Win= Win +1
  elif playerMove == 'p' and computerMove=='r':
    print('You won!')
    Win= Win +1
  elif playerMove == 'p' and computerMove=='s':
    print('You lost!')
    Loss= Loss + 1
  elif playerMove=='s' and computerMove=='r':
    print('You lost!')
    Loss= Loss +1
  elif playerMove=='s' and computerMove=='p':
    print('You won!')
    Win= Win +1

    
    

      

    

      

import random, sys
Win= 0
Loss= 0
Tie= 0
print('ROCK, PAPER, SCISSORS')
while True:
  print('%s Wins,%s Losses,%s Ties' %(Win, Loss, Tie))
  while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove= input()
    if playerMove == 'q':
      sys.exit()
    elif playerMove== 'r' or playerMove=='p' or playerMove=='s':
      break
    print("please type one of r, p, s or q.")

  if playerMove == 'r':
    print('ROCK versus...')
  if playerMove =='p':
    print('PAPER versus...')
  if playerMove =='s':
    print('SCISSORS versus...')

  randomNumber = random.randint(1,3)

  if randomNumber== 1:
    computerMove='r'
    print('ROCK')
  elif randomNumber==2:
    computerMove='p'
    print('PAPER')
  elif randomNumber==3:
    computerMove='s'
    print('SCISSORS')
  if playerMove == computerMove:
    print('It is a tie!')
    Tie= Tie +1
  elif playerMove =='r' and computerMove=='p':
    print('You lost!')
    Loss= Loss +1
  elif playerMove =='r' and computerMove=="s":
    print('You won!')
    Win= Win +1
  elif playerMove == 'p' and computerMove=='r':
    print('You won!')
    Win= Win +1
  elif playerMove == 'p' and computerMove=='s':
    print('You lost!')
    Loss= Loss + 1
  elif playerMove=='s' and computerMove=='r':
    print('You lost!')
    Loss= Loss +1
  elif playerMove=='s' and computerMove=='p':
    print('You won!')
    Win= Win +1

    
    

      

    

      
