#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 00:56:46 2025

@author: samandaroripov
"""

art='''       ___________
       \         /
        )_______(
        |"""""""|_.-._,.---------.,_.-._
        |       | | |               | | ''-.
        |       |_| |_             _| |_..-'
        |_______| '-' `'---------'` '-'
        )"""""""(
       /_________\
       `'-------'`
     .-------------.
    /_______________\
'''

print(art)

value = {}
while True:
    name = input('What is your name?: ')
    price = int(input('What is your bid price?: $'))
    
    value[name] = price
    
    others = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if others == 'yes':
        print('\n'*100)
        continue
    elif others == 'no':
        max_key = max(value,key=value.get)
        max_value = value[max_key]
        print(f'The winner is {max_key.title()} with a bid of ${max_value}')
        break
    else:
        print('\n'*100)
        print('Invalid entry')
        continue
        