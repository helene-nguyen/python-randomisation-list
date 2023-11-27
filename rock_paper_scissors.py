"""
Rules:
Rock wins against scissors
Scissors win against paper
Paper wins against rock
"""

import random

random_player_choice = random.randrange(1, 3)

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


def play():
    """
    Play the game
    """
    game_images = [rock, paper, scissors]

    adversary = random.randrange(0, 2)
    my_choice = int(input('My choice between 0=rock, 1=paper, 2=scissors: '))

    print(f'My adversary: {game_images[adversary]}')
    print(f'Me: {game_images[my_choice]}')

    if my_choice == adversary:
        print("It's draw")
    elif (adversary == 0 and my_choice == 1) or (adversary == 1 and my_choice == 3):
        print("You win")
    else:
        print("You lose")


play()
