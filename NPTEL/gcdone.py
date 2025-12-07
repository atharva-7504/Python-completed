# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:04:09 2025

@author: Atharva
"""

def gcd(m,n):
    fm = []
    for i in range (1,m+1):
        if ( m % i ) == 0 :
            fm.append(i)
    fn = []
    for j in range (1,n+1):
        if( n % j )== 0:
            fn.append(j)
    cd = []
    for f in fm:
        if f in fn:
            cd.append(f)
    return(cd[-1])
    
m = int(input("Enter value of m :"))   
n = int(input("Enter value of n :"))   

oo = gcd(m, n)
print(f"The greatest common divisor from {m} and {n} is : {oo}") 
    
      