#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 13:41:19 2025

@author: samandaroripov
"""

print('''**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print('Welcome to the Treasure Island!')
print('Your mission is find the treasure.')

direction = input('You are at the crossroad, where do you want to go.\nType "left" or "right":\n')


if direction.lower() == 'left':
    
    way = input('''You\'ve come to a lake. There is an island in the middle of the lake.\n
Type "wait" to wait for a boat. Type "swim" to swim across:\n''')
    
    if way.lower() == 'wait':
        color = input('''You arrive at the island unharmed. There is a house with 3 doors.\n
One red, one yellow and one blue. Which color do you choose?:\n''')
        
    
        if color.lower() == 'yellow':
            print('You found the treasure! You Win!')
        
        elif color.lower() == 'red':
            print('You got burned by fire.Game Over.')
        
        elif color.lower() == 'blue':
            print('You got attacked by beasts.Game Over.')
        
        else:
            print('Game over.')
    
    
    else:
        print('You get attacked by an angry trout. Game Over.')

else:
    print('You fell into hole.Game over.')

    





























