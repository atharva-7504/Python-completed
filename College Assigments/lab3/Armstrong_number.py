# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:03:57 2025

@author: Atharva
"""

num = int(input("Enter the number :"))
length = len(str(num))
sum = 0
temp = num
while temp> 0:
    digit = temp % 10
    sum = sum + digit ** length
    temp = temp // 10
    
print("Number is {} and sum is {}".format(num, sum))
if sum == num:
    print("Armstrong number .")
else:
    print("Not an armstrong number.")
    
    