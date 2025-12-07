# #Check whether the number is +ve, -ve, or 0
# num1 = int(input("Enter any numeric value :"))
# if(num1 > 0):
#     print(num1,"is positive number")
# elif(num1==0):
#     print(num1,"is equal to 0")
# else:
#     print(num1,"is negative number")
# print("The program is executed")

# # # Check whether the no is even or odd?

# num = int(input("Enter any numeric values:"))
# if(num % 2 == 0):
#   print("The number given is even")
# else:
#     print("The number given is odd")
# print("Program Executed")

# # #Write a program to find largest among three numbers?

# num_1 = int(input("Enter the first number :"))
# num_2 = int(input("Enter the second number :"))
# num_3 = int(input("Enter the third number :"))
# if(num_1 > num_2 and num_1 > num_3):
    
#     print(num_1,"largest number among the three number")

# elif(num_2 > num_3 and num_2 > num_1):
#     print(num_2,"largest number among the three number")
# else:
#     print(num_3,"largest number among the three numbers")
# print("The program is executed")

# # # check smallest number.
# num1 = int(input("Enter the first number :"))
# num2  = int(input("Enter the second number:"))
# num3  = int(input("Enter the third number:"))
# if(num1<num2 and num1<num3):
#                  print(num1,"is the smallest number among the three numbers:")
# elif(num2<num1 and num2<num3):
#     print(num2,"is the smallest number among the three numbers:")
# else:
#   print(num3,"is the smallest number among the three numbers:")
# print("The program is executed")

# # Degree conversion.
# degree_Fahrenheit = eval(input("Enter your Temperature in Fahrenheit:"))
# degree_Celcius = 5/9*(degree_Fahrenheit - 32)
# print("Your Fahrenheit temperature in Celcius is ",round(degree_Celcius))


# # # Check Whether number is spy or not 

# num = int(input("Enter the number :"))
# add = 0
# product = 1
# temp = num
# while num != 0:
#      remainder = num % 10
#      add = add + remainder
#      product  = product * remainder
#      num = num // 10
# if add == product :print(f"The number {temp} is a SPY number.")
# else:print(f"The number {temp} is not a SPY number.")
     

# # 2nd method
# num = input("Enter a number :")
# add = 0
# product = 1

# for digit in num :
#      add = add + int(digit)
#      product = product * int(digit)

# if add == product: print("SPY")
# else: print("Not a Spy")



# # Write a program  for finding Armstrong numer 
# num = int(input("Enter any number :"))
# temp = num
# sum = 0
# no_of_digits = len(str(num))
# while temp>0:
#      digit = temp % 10
#      sum += digit**no_of_digits
#      temp = temp // 10
# if num == sum:print(f"The number {num} is an Armstrong Number.")
# else:print(f"The number {num} is not an Armstrong number.")
# print("o")



def greet(name):
        """ This is to greet when argument is passed"""
        print("Hello",name)
name = "Atharva"
greet(name)
print(greet.__doc__)