# import sys 
# print("Start")
# try:
#     n1 = int(input("Enter first number :"))
#     n2 = int(input("Emter the second number :"))
#     ans = x/y
#     print(f"{x}/{y} = {ans}")
# except:
#     print("Exception caught")
#     print("Error Type ::",sys.exc_info()[0])
#     print("Error Desc ::",sys.exc_info()[1])
# print("End") 




# print("Start")
# try:
#     x = int(input("Enter first number :"))
#     y = int(input("Enter second nmber :"))
#     ans = x/y
#     list = []
#     print("Values at indec 1::",list[1])
#     print(f"{x} / {y} = {ans}")
# except ZeroDivisionError:
#     print("Cannot divide number by zero")
# except NameError:
#     print("Invalid object/var name ")
# except ValueError:
#     print("Invalid input given")
# except Exception:
#     print("Inside the generic handler.")



# print("Start")
# try:
#     x = int(input("Enter first number :"))
#     y = int(input("Enter second nmber :"))
#     ans = x/y
#     list1 = []
#     print("Values at indec 1::",list1[1])
#     print(f"{x} / {y} = {ans}")
# except ZeroDivisionError as e:
#     print("Error Desc:",e)
# except NameError as e:
#     print("Error Desc: ",e)
# except ValueError as e:
#     print("Error Desc:",e)
# except Exception as e:
#     print("Generic handler Desc:",e)
# print("End")

# print("Start")
# try:
#     x = int(input("Enter first number :"))
#     y = int(input("Enter second nmber :"))
#     ans = x/y
#     list1 = []
#     print("Values at indec 1::",list1[1])
#     print(f"{x} / {y} = {ans}")
# #multiple handling of excetions using tupples.
# except (ZeroDivisionError,ValueError,NameError,TypeError) as e:
#     print("Error Desc:",e)
# except Exception as e:
#     print("Generic handler Desc:",e)
# print("End")


# try : # After try except or finally is optional 
#     ""
# except:
#     ""
# else:
#     ""    # (optional)executes only when there is no exception raised by try  block 
# finally:
#     ""    #(optional) Always executes but must be only one finally block 
#           # to release occupied resources 
#           #   if exception is in finally block 


# print("Start")
# try:
#     print("Inside try block")
#     ans = 10/0;
#     print("Answer ==",ans)
#     print("End of try block")
# except Exception as e:
#     print("Error caught in generic handler ")
# else:
#     print("Inside else block ")
# finally:
#     print("Inside finally block")
# print("End")


# print("Start")
# try:
#     print("Inside try block")
#     ans = 10/0;
#     print("Answer ==",ans)
#     print("End of try block")
# except Exception as e:
#     print("Error caught in generic handler ")
# else:
#     print("Inside else block ")
# finally:
#     print("Inside finally block")
# print("End")



# print("Start")
# try:
#     print("Outer::try")
#     try:
#         print("Inner::try")
#         ans = 10/2
#         print("Answer = ",ans )
#         print("End of inner try block")
#     except ValueError as e:
#         print("Inner Exception Decs ::",e)
#     finally:
#         print("Inner :: finally")
# except ZeroDivisionError as e:
#     print("Outer Exception Desc ::",e)
# except Exception:
#     print("Outer Generic header Desc ::",e)
# finally :
#     print("Outer finally ")
# print("End")
