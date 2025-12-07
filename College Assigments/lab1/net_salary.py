# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:31:24 2025

@author: Atharva
"""

basic_salary = eval(input("Enter the annual income in Rs. :"))
HRA = 0.1 * basic_salary
TA = 0.05 * basic_salary

gross_salary = basic_salary + HRA + TA

professional_tax = 0.02 * gross_salary

net_salary = gross_salary * professional_tax

print(f"Gross salary is Rs. :{gross_salary}")
print(f"Net salary is Rs. :{net_salary}")
