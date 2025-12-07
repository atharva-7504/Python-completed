# class Car():
#     def __init__(self):
#         self.name = input("Enter Car name:")
#         self.brand = input("Enter Car brand :")
#         self.color = input("Enter Car color :")
#         self.cost = int(input("Enter the cost of the car in Rs."))
#         return
#     def display_details(self):
#         print(f"NAME : {self.name}  BRAND : {self.brand}  COLOR : {self.color}  COST : {self.cost}")
# print("         CAR DETAILS         ")
# print("====================================")
# car1 = Car()
# car2 = Car()
# car3 = Car()
# car1.display_details()
# car2.display_details()
# car3.display_details()

# '''-----------------------------------------------------------------------------------------------------'''

# class Employee():
#     def __init__(self):
#         self.employee_name = input("Enter employee name :")
#         self.employee_id = int(input("Enter employee id:"))
#         self.employee_salary = int(input("Enter employee salary:"))
#         return
#     def printData(self):
#         print(f"NAME : {self.employee_name}  ID : {self.employee_id}  Salary :{self.employee_salary}")
# e1 = Employee()
# e2 = Employee()
# print("     Employee Details     ")
# print("==============================")
# e1.printData()
# e2.printData()


# class MyClass():
#     def __init__(self):
#         self.name = "Atharva"
#         self.roll_no = 42
#         return
# student = MyClass()
# print(hasattr(student,"roll_no"))
# print(getattr(student,"roll_n","default"))
# print(setattr(student,"name","G"))
# print(student.name)
# print(delattr(student,"roll_no"))
# print(student.roll_no)

#Multiplication table
for i in range(1,11):
    print(f"Table of {i} : ")
    for j in range(1,11):
        print(f"{i} x {j} : {i*j}")
    print()

for i in range(1,4):
    print("*"*i)



s = input("Enter the string :")
char = input("Enter the character to count :")
count = 0
for c in s:
    if c == char:
        count += 1
print(f"{char} appears {count} times.")
