import random

while True:
    player = input('Enter a number from 1 to 10: ')
    computer = random.randint(1, 10)
    while player != 'q':
      if player == computer:
        print('You guessed right!')
        break
      else:
        print('Invalid guess')
    break