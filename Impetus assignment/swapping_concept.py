# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:06:41 2025

@author: Atharva
"""
# age = 18
# per = 67.45677
# name = "Rahul"
# print(" Hey " name ". You are"  "years old")
# print("Hey " + name +  )

# for printing multiple values using % function
# print("Hey %s You are %d years old." %(name , age))

# print("You scored %f %% " %per)
# print("You scored %.2f %% " %per)   # field width concept

# name = input("Enter Name :")
# print(name , "Welcome to Impetus")
# age = int(input("Enter your age :"))




# Write a python script to accept integers from the user and swap their values

#using third variable
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
print("num1 before swapping is:",num1)
print("num2 before swapping is:",num2)
swap = num1
num1 = num2 
num2 = swap
print("num1 after swapping is:",num1)
print("num2 after swapping is:",num2)

#without using third variable
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
print("num1 before swapping is:",num1)
print("num2 before swapping is:",num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2 
print("num1 after swapping is:",num1)
print("num2 after swapping is:",num2)
bin(-23)
print(bin(-23))
x = input("x = ")
y = input("y =")
x = x^y 
y = x^y
x = x^y



x,y = y,x
print(x)
print(y)


# Write a python script to accept radius of the circle from the user 

from math import *
radius = eval(input("Enter the radius of circle :"))
area = pi * radius*radius
print("Area of the circle is : %.3f" % area)

age = int(input("Enter the age of the Voter :"))
print("Age of the Voter is ",age)
if (age >= 18):
    print("Voter is Eligible for voting.")
else:
    print("Voter is not Eligible for voting.,Sorry")
    

# We can use semicolun also ;
num = eval(input("Enter the number :"))
if ( num>0 ):
    print(num,"Is a positive number ");
elif( num<0 ):
    print(num,"It is a negative number ");
else:
    print("It is a 0.");
    
    
#Ternary ?:
num = 20
print("Yes") if num > 10 else print("No")