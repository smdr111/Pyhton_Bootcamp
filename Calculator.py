#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 14:22:05 2025

@author: samandaroripov
"""

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {'+' : add,
             "-" : subtract,
             '*' : multiply,
             '/' : divide
             }
def calculator():
    n1 = float(input("What's the first number?: "))
    while True:
        
        operation = input('+\n-\n*\n/\nPick an operation: ')
        
        n2 = float(input("What's the next number?: "))
        
        result = operations[operation](n1,n2)
        print(f'{n1} {operation} {n2} = {result}')
        
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        
        if answer == 'y':
            n1 = result
        else:
            calculator()
        
  
    



