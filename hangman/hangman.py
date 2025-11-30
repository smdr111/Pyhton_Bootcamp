#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:59:07 2025

@author: samandaroripov
"""
import random
from hangman_words import words
from stages import stages
from logo import log

print(log)

word = random.choice(words)
print(word)

line = '-'*len(word)
print(f'Word to guess: {line}')

correct_letters = []

limit = 6

while limit>0:
    display = ''
    guess = input('Guess a letter: ').lower()

    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    for i in word:
        if i == guess:
            display += i
            correct_letters.append(i)
        
        elif i in correct_letters:
            display += i
        else :
            display += '-'
    print(display)
    print(stages[limit])

    
    if guess not in word:
        limit -= 1
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        if limit == 0:
            print(f'**********IT WAS {word}! You Lose**********')
            break
    print(f'**********{limit}/6 LIVES LEFT**********')
    
    if display == word:
        print(f'**********IT WAS {word}! You won**********')
        break
    
    print(f'Word to guess: {display}')
    
        
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
