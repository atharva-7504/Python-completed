# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:28:06 2025

@author: Atharva
"""

# Program to perform all operations 

def calculation(num1,num2):
    add = num1 + num2 
    sub = num1 - num2
    div = num1 / num2
    mul = num1 * num2
    mod = num1 % num2
    print(f"Addition of {num1} and {num2} is : {add}")
    print(f"Substraction of {num1} and {num2} is : {sub}")
    print(f"Multiplication of {num1} and {num2} is : {mul}")
    print(f"Division of {num1} and {num2} is : {div}")
    print(f"Modulus of {num1} and {num2} is : {mod}")
    
num1 = eval(input("Enter first numeric value :"))
num2 = eval(input("Enter second numeric value :"))
cal = calculation(num1, num2)