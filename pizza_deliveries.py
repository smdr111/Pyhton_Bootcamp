#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 01:12:18 2025

@author: samandaroripov
"""

print('Welcome to the pizza deliveries!')
size = input('What size pizza would you like? S,M or L?: ')
pepperoni = input('Would like to add pepperoni? Y or N?: ')
extra_chz = input('Would you like extra cheese? Y or N?: ')

if size == 'S':
    bill = 15
    if pepperoni=='Y':
        bill+=2
elif size == 'M':
    bill=20
    if pepperoni=='Y':
        bill+=3
elif size == 'L':
    bill=25
    if pepperoni=='Y':
        bill+=3
if extra_chz=='Y':
    bill+=1
print(f'Your total bill is {bill}$')
