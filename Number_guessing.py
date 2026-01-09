#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 14:24:53 2026

@author: samandaroripov
"""
import random as r



def guess_num():
    numbers = list(range(1,101))
    return r.choice(numbers)


def level():
        level = input("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard':  """).lower()
        if level == 'easy':
            return 10
        elif level == 'hard':
            return 5
        else:
            return None

attempt = level()
number = guess_num()

while attempt>0:
    guess = int(input(f"You have {attempt} attempts remaining to guess the number.\nMake a guess: "))
    
    
    if attempt == 1 and guess != number:
        print('You have run out of guesses. You Lose!')
        break
    
    elif guess < number:
        print('Too low.\nGuess again.')
        attempt -= 1
        continue
    
    elif guess > number:
        print('Too High.\nGuess again.')
        attempt -= 1
        continue
    
    elif guess == number:
        print(f'You got it! Answer was {number}!')
        break
    
    
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    

