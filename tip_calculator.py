#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 22:52:12 2025

@author: samandaroripov
"""
print('Welcome to the tip calculator!')
total = float(input('What was the total bill today?\n'))
percent = int(input('How much tip would you like to give(in percent)? 10,12 or 15?\n'))
num_people = int(input('How many people to split the bill?\n'))
print(f'Each person should : {(total + (total*percent/100))/num_people}')