# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:35:14 2025

@author: Atharva
"""

# list1  = [1,2,5,6]
# list2 = list1 
# list1[2] = 7 #changing value in list1
# print(list1)
# print(list2) #no change in list2

# list1 = [1,3,5,6]
# list2 = list1
# list1 = list1[0:2] + [6] + list1[3:]  #concatenation of list
# print(list1)  #change

# print(list2)  #because of + operator the is change

# list1 = [1,3,5,6]
# list2 = list1


#-----------------------List Functions------------------------
my_list = list(range(0,10))
print(my_list)

my_list.append(10)
print(my_list)

my_list.extend([11,12])
print(my_list)

my_list.insert(13,13)
print(my_list)

my_list = my_list + my_list
print(my_list)

my_list.remove(5)
print(my_list)