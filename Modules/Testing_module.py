# import module1
# import module2
#=============================================================================
# "Importing multiple modules at one go :"
import module1,module2
print("Contents available to access",dir()) # directory to check content available to use
print("File Path ==",__file__)  #gives path of the file where content of file is stored
print("Module Name ==",__name__)  #by default __main__
print("Module Name ==",__name__)
print("Name of module1 ::",module1.__name__)


# ==================================================================================================

import test1
print("Contents available to access::\n\n",dir())
# print("Value of x =",x) # Error x not defined
