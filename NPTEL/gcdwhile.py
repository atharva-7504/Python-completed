# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:28:51 2025

@author: Atharva
"""

def gcd(m,n):
    i = min(m,n)
    while i > 0:
        if ( m % i)==0 and (n % i) == 0:
            return(i)
        else:
            i -= 1
            
m = int(input("Enter value of m :"))   
n = int(input("Enter value of n :"))   

oo = gcd(m, n)
print(f"The greatest common divisor from {m} and {n} is : {oo}") 

    
      