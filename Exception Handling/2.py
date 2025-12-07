# def Div(x,y):
#     print("Inside Div() function")
#     try:
#         print("Inside Div::try")
#     except ZeroDivisionError as e :
#         print("Div::Error Desc::",e)
#         ans = x/y
#         print("Answer =",ans)
#     finally:
#         print("Inside Div::finally")
#     return
# print("Start of main block")
# try:
#     print("Inside main::try")
#     Div(10,0)
# except ZeroDivisionError as e:
#     print("Main::error Desc:",e)
# except Exception as e:
#     print("Exception Desc::",e)
# finally:
#     print("main::finally")
# print("End of the main block")



#User defiend Exception : we need to raise 
# class MyException(Exception):
#     def __init__(self):
#         self.errmsg = "Error Occured"
#         return
# print("Start")
# try:
#     print("Inside try block")
#     raise MyException()
# except MyException as e:
#     print("Error Desc ::",e.errmsg)
# except Exception as e:
#     print("Generic Handler Err Desc.::",e)
# finally:
#     print("Inside finally block")
# print("End")



#Write a program that accepts strig from the user .If entered string consists
# number,then throw user defined Exception  as "NameNotProperEXception".

# class NameNotProperException (Exception):
#     def __init__(self):
#         self.msg = "Number exists in string."
#         return
# print("Start")
# s = input("Enter any string :")
# try:
#     print("Inside Try Block")
#     if s.isalpha() == True:
#         print("Valid")
#     else:
#         raise NameNotProperException()
# except NameNotProperException as e:
#     print("Desc of Error ::",e.msg)
# except Exception as e :
#     print("Exception Desc::",e)
# finally:
#     print("Final Block")
# print("End")



#Write a program to find Exception Marks out of Bounds Create a Class student 
# if marks is greater than 100, it must generate user defined exception called 
# "MarksOutOfBoundsException"

class MarksOutOfBoundsException (Exception):
    def __init__(self):
        self.errmsg = "Marks is above 100,Error Generated !"
        return
class Student :
    def __init__(self):
        s











