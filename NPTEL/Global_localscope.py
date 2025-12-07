# x = 4   #global variable
# print(x)

# def hello():
#     global x
#     x = 10    
#     print("The local x is",x)
#     y = 7   #local variable 

# hello()
# print("The global x is",x)
# print(y) # error because y is local variable and this variable are printed inside function only 



# Nested function
def f():
    def g(a):
        return(a+1)
    def h(b):
        return(b*2)
    global x  
    y = g(x) + h(x)
    print("The value of y inside function ",y)
    x = 34  # changing value of global var x 

x = 7
f()
print("The value of x",x)