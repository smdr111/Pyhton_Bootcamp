#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 12:41:24 2026

@author: samandaroripov
"""
vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
from game_data import data



def generate():
    return random.choice(data)

A = generate()

x = 1

score = 0

while True:
    print(f'{x}-Round\n')
    
    B = generate()
    
    print(f'Compare A: {A["name"]},{A["description"]},from {A["country"]}.')
    
    print(vs)
    
    print(f'Compare B: {B["name"]},{B["description"]},from {B["country"]}.')
    
    winner = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if winner == 'a' and A['follower_count'] > B['follower_count']:
        x += 1
        score += 1
        print(3*'\n')
        print(f"You're right! Current score: {score}.\n")
        continue
    
    elif winner == 'b' and A['follower_count'] < B['follower_count']:
        A = B
        x += 1
        score += 1
        print(3*'\n')
        print(f"You're right! Current score: {score}.\n")
        continue
    
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        
        break
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

