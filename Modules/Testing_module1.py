# import module1
# import module2
#=============================================================================
# "Importing multiple modules at one go :"
# import module1,module2
# print("Contents available to access",dir()) # directory to check content available to use
# print("File Path ==",__file__)  #gives path of the file where content of file is stored
# print("Module Name ==",__name__)  #by default __main__
# print("Module Name ==",__name__)
# print("Name of module1 ::",module1.__name__)


# ==================================================================================================

# import test1
# print("Contents available to access::\n\n",dir())
# print("Value of x =",test1.x) # Error x not defined
# print("Value of _y = ",test1._y)

#=====================================================================================================

# from test1 import *  # * is used to import all public data no private data available
# from test1 import _y,__z

# print("Contents available to access ::\n\n",dir())
# show()
# print("Value of x =", x)
# print("Value of _y =", _y) # Error - not available 
# print("Value of __z =", __z) # Error

#=====================================================================================================
# from test1 import *
# from test2 import *

# print("Contents available to access ::\n\n",dir())
# display()
# show() # Latest definition of show() will be executed from test2 and not from test1
#----------------------------------------------------------------------------------------------------
# import test1,test2

# '''Explicity accessing the functions from the modules to avoid overwriting of function definitions'''
# test1.show()
# test2.show()

#======================================================================================================

# import module2 as m2   # we can change name of module 
# print("Contents available to access ::\n\n",dir())


#======================================================================================================
# from array import *
# arr = array("b",[1,2,3,5,6,7,28,100,125,-128])  # max = 127 min = -128
# print(arr)

# from array import *
# arr = array("B",[1,2,3,5,6,7,28,100,125,128,245,255])  # max = 255 min = 0
# for val in arr:
#     print(val)
