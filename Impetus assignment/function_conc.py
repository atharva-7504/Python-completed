
# def edu_loan(principal,rate,duration = 3): # Default parameters to a function must be set to right to left order
#     print("Fees :",principal)
#     print("Rate of interest :",rate)
#     print("Duration :",duration)

# principal =120000
# rate = 2.5
# edu_loan(principal,rate)


# ==============================================================================================

# def show(name,roll,per):   #keyword are required and must be same 
#                            # function with keyword arguments
#     print("Name :",name)
#     print("Roll :",roll)
#     print("Per :",per)
# show(name="Atharva",roll=42,per=9.27)
# show(name="Om",roll=46,per=9.09)

# =================================================================================================

# Function with Variale length'POSITIONAL' arguments 

# def show(*args):
#     print("show() function called ......")
#     print("\n Type of args",type(args))
#     print("Value in args ==> ",args)
#     for val in args:
#         print("Value :",val)
#     return
# show()
# show(100)
# show(1,5,"Hello",3.2)

# ==============================================================================================

# def show(name,roll,*subjects):   # * used fro n no of position argumnets 
                                   # ** used for n no of keyword arguments
#     print("Name :",name)
#     print("Roll :",roll)
#     print("Subjects :",*subjects)
#     return
# show("Atharva",42,("m1,eg,em,bxe,bee,chem,physics"))


# def show(**kwargs):
#     print("Type of kwargs:",type(kwargs))
#     print("Data ::",kwargs)
#     data = kwargs.items()
#     for key,val in data:
#         print(key.upper(),"==",val)
#     return
# show(roll=42,name="Atharva",per=9.3)

# def show(name, roll, **subjects):
#     print("Roll :",roll)
#     print("Name :",name)
#     data = subjects.items()

#     for sub,marks in data:
#         print(sub.upper(),"==",marks)

# show(roll = 101 , name = "Krishna" , phy=83,maths=91,chem = 65)

#==========================================================================================================

# Both positional and key arguments 
# positional arguments should be followed by keyword parameters.

# def show(roll,name,per,city):
#     print(roll,name,per,city)
#     return
# show(101,"rahul",city="Pune",per=9.9)

#==========================================================================================================



# Wite a python program to sum all elements in a list .
# def sum_(list1):
#     _sum = sum(list1)
#     print("Sum of the list :",_sum)

# list1 = [6,-2,15]
# sum_(list1)


# Write program to add the values if int values taken from user.
# def add(*args):
#     sum1 = 0
#     for val in args :
#         if type(val) == int:
#             sum1 += val
#     print("ADDITION ==> ",sum1)
# add(19.4,3,2,4,5,[6,7],(5),"Hi")


#=================================================================================================

# Local / Global Variables

#------------------------------------------
# x = 10  # global
# print("First : x ==> ",x)
# def show():
#     x = 99 # local to show() function
#     print("show() : x ==>",x)
#     return
# print("Second : x ==>",x) 
# show()
# print("Third : x ==>",x)

#--------------------------------------

# x = 10  # global
# print("First : x ==> ",x)
# def show():
#     global x
#     x = 99 # local to show() function
#     print("show() : x ==>",x)
#     return
# print("Second : x ==>",x) 
# show()
# print("Third : x ==>",x)

#-----------------------------------------

# roll = 42
# name = "Krishna"

# def show():
#     per = 7.8
#     print(locals())
#     return 
# print("Till this line,I can access ::\n",globals())

# num =1 
# def add():
#     num = 2
#     print(globals())
#     sum = num + globals()["num"]
#     print("Sum :",sum)
#     return
# add()

for i in range(1,15):
    print("Ak"*i)