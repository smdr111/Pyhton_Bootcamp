#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 12:49:55 2025

@author: samandaroripov
"""
from art import logo
import string


print(logo)


alphabet = list(string.ascii_lowercase)


def ceaser(direction,original_text,shift_amount):
    result = ''
    
    if direction == 'decode':
        shift_amount *= -1
            
    for i in original_text:
        if i not in alphabet:
            result += i
        else:
            shift = alphabet.index(i)+shift_amount
            shift %= len(alphabet)
        
            result += alphabet[shift]
    
    print(f"Here's the {direction}d result: {result}")

    


while True:
    direction = input('Type "encode" to encrypt, type "decode" to decyrpt:\n').lower()
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    
    ceaser(direction, text, shift)
    
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if answer == 'no':
        break
    














