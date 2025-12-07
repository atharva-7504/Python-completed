# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:18:50 2025

@author: Atharva
"""


# def calculator(num1,num2):
#     addition = num1 + num2
#     substraction = num1 - num2
#     product = num1*num2
#     divide = num1 / num2
#     return addition 
#     return addition 
#     return product 
#     return divide

    

# num1 = int(input("Enter first number : "))
# num2  = int(input("Enter second number : "))
# addition = calculator(num1,num2)
# substraction = calculator(num1,num2)
# product = calculator(num1,num2)
# divide = calculator(num1,num2)
# print(f"Addition of two numbers is {calculator}")
# print(f"Substraction of two numbers is {calculator}")
# print(f"Multiplication  of two numbers is {calculator}")
# print(f"Division of two numbers is:{calculator}")


# write a function to find largest of three numbers 1 time input,
# write a function to print multiiplication table of particular number take from user input1  time , 2nd function 
# write a function to find sum of digit of number taken 2 diff fun



# def largest_numbers(num1,num2,num3):
#     if(num1 > num2 and num1 > num3):
#         print(f"{num1} is the largest number among {num2} & {num3}. ")
    
#     elif(num2 > num1 and num2 > num3):
#         print(f"{num2} is the largest number among {num1} & {num3}.")
   
#     elif(num3 > num1 and num3 > num2 ):
#         print(f"{num3} is the largest number among {num1} & {num2}. ")
#     elif(num1 == num2 or num1 == num3 or num2 == num3):
#         print("Entered numbers {} and {} are equal".format('num1','num2','num3'))
        
# def smallest_numbers(num1,num2,num3):
#     if(num1 < num2 and num1 < num3):
#         print(f"{num1} is the smallest number among {num2} & {num3}. ")
    
#     elif(num2 < num1 and num2 < num3):
#         print(f"{num2} is the smallest number among {num1} & {num3}.")
   
#     else:
#         print(f"{num3} is the smallest number among {num1} & {num2}. ")
        
# if __name__ == "__main__":
#     num1 = int(input("Enter the first number :"))
#     num2 = int(input("Enter the second number :"))
#     num3 = int(input("Enter the third number :"))
    
#     largest_number = largest_numbers(num1,num2,num3)
#     smallest_number = smallest_numbers(num1, num2, num3)
    


# def table(num):
#     for i in range(1,11):
#         print(f"{num} x {i} = {i*num}")
# if __name__ == "__main__" :       
#    num = int(input("Enter the number to find multiplication table : "))        
#    multiplication_table = table(num) 
# #    print(multiplication_table)
    



# def sumof(num):
#     for i in range(0,num):
#         i += 1
   
    

# if __name__ == "__main__":
#     num = int(input("Enter a number to find sum till number :"))
#     sum = sumof(num)
#     print("Sum of number is :",sum)
        

# Lambda Function : We can take one or more arguments but only one executable expression written after (:)

# sqr = lambda num : num*num
# num = eval(input("Enter a number :"))
# ans = sqr(num)
# print("Square of the number is :",ans)

# Write a python code to take three number from user and do its sum .
# sum = lambda num1,num2,num3 : num1+num2+num3
# num1 =eval(input("Enter a number :"))
# num2 = eval(input("Enter a number :"))
# num3 = eval(input("Enter a number :")) 
# ans = sum(num1,num2,num3)             
# print(f"Sum of {num1}+{num2}+{num3} : {ans}")




# def addition(*args):
#     print(sum(args))

# add = lambda *args : sum(args)
# ans = add(1,2,3,4,5,6,7,8,9)

# print("additon : ",ans)



# Write a python code to accept to numbers and return maximum using lamda function.

# l1 = []
# maximum = lambda num1,num2 : l1.extend(num1,num2)
# ls = l1.sort()
# result = ls[:-1]

# num1 = eval(input("Enter 1st number :"))
# num2 = eval(input("Enter 2nd number :"))
# print(f"Max Value from {num1} and {num2} : {result}")


# max_value = lambda x,y :x if x>y else y    # Ternary operator 
# ans = max_value(10,20)
# print("Max :",ans)


# Nested lambda function    

sqr = lambda x : x**2
print("Square of number is",sqr(5))
cube =  lambda x : sqr(x)*x
print("Cube of number is",cube(5))

