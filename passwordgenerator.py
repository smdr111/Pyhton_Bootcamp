#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 13:44:44 2025

@author: samandaroripov
"""
import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

num_letters = int(input('Welcome to the password generator!\n'
                   'How many letter would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like?\n'))
num_numbers = int(input('How many numbers would you like?\n'))

if 0<num_letters<=len(letters) or 0<num_symbols<=len(symbols) or 0<num_numbers<=len(numbers):
        password = random.sample(letters,num_letters) + random.sample(symbols,num_symbols) + random.sample(numbers,num_numbers)
        print(password)
        random.shuffle(password)
        
        print(password)
        
        result = ''.join(password)
        
        print(f'Your password is: {result}')
else:
    print('Invalid number!')











