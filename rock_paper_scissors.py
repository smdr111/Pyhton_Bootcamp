#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 13:26:44 2025

@author: samandaroripov
"""
import random as r

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_list = [rock,paper,scissors]

player = int(input('What do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors:\n'))
computer = r.randint(0,2)

if player<0 or player>2:
    print('Invalid number!')
else:
    c_choice = game_list[computer]
    pl_choice = game_list[player]
    
    print(pl_choice)
    print(f'Computer chose :\n{c_choice}')
    
    if player == computer:
        print('It is draw!')
    elif (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
        print('You won!')
    else:
        print('You lose!')

























