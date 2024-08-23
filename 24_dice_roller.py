import random

p1 = random.randint(1, 6)
p2 = random.randint(1, 6)

if p1 > p2:
    print('Player 1 wins!')
elif  p1 < p2:
    print('player 2 wins')
else:
    print('Draw!')
