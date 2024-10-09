#ROCK, PAPER, SCISSORS

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player = int(input('Choose 0 for rock, 1 for scissors, 2 for paper: '))

images = [rock, scissors, paper]

computer = random.randint(0, 2)

print(f"You chose {images[player]}")

print(f"Computer chose {images[computer]}")


if player == computer:
    print('draw')
elif player == 0 and computer == 1 or player == 2 and computer == 0 or player == 1 and computer == 2:
    print('You win')
else:
    print('Computer wins')
