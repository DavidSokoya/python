import random

choices = ['rock', 'paper', 'scissors']
def get_valid_input():
   while True:
      player = input("Enter rock paperor scissors, or 'q' to quit: ").lower()
      if player  in choices or player == 'q':
         return player
      else:
         print('Invalid input.. Please enter rock paper or scissors')

while True:
    player = get_valid_input()
    if  player == 'q':
        break
    computer = random.choice(choices)
    if player == computer:
      print('Draw!')
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
      print(f"player: {player} vs computer: {computer} => player won!")
    else:
      print(f"player: {player} vs computer: {computer} => Computer won!")