# for x in range(3,8):
#     for y in range(5,9):
#         if x*y > 8:
#             break
# print(x*y)

# list1 = [1,3]
# list2 = list1
# list1[0] = 4
# print(list2)

# s ="Welcome"
# print(s[:6] + "Impetus")

# stud = {
#     101:"Shital",
#     102:"Khushichandra",
#     103:"Shubra",
#     104:"Shital",
# }
# print("Name:",stud[2])

# print(0xA + 0xB + 0xc)

# x = 'abcd'
# for i in range(len(x)):
#     i.upper()
# print(x)

value = 80
def display(n):
    global value
    value = 15
    if n%4 == 0:
        value += n
    else:
        value -= n
print(value,end="#")
display(20)
print(value)


def foo():
    try:
        return "Pune"
    finally:
        return "Mumbai"
city = foo()
print(city)

litt = [1,3,2]*2
print(litt)

import random
a = random.randint(3,5)
b= random.randint(2,3)
c = a+b
print(c)

class Demo(object):
    print("Iside class ")
Demo()
Demo()
obj = Demo()