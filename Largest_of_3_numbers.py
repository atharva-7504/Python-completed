# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:18:08 2024

@author: Atharva
"""

def get_integer()->int:
   
    num1 = (input("Enter the first number: "))
    num1.isdigit()
    print("Error")
    print(input("Enter first number :"))
    num2 = (input("Enter the second number: "))
    num2.isdigit()
    print("Error")
    print(input("Enter second number :"))
    num3 = (input("Enter the third number: "))
    num3.isdigit()
    print("Error")
    print(input("Enter third number :"))
    
def largest_of_three(num1:int,num2:int,num3:int):
    if num1 > num2 and num1 >num3:
        print(f"{num1} is largest among the three numbers: ")
    elif num2 > num1 and num2 >num3:
        print(f"{num2} is largest among the three numbers: ")
    else:
        print(f"{num3} is largest among the three numbers: ")
        
if __name__=="__main__":
    num1,num2,num3 = get_integer()
    largest_of_three(num1,num2,num3)
    
    
