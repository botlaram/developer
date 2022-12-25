##decorator is used to add functionality to an existing code.

def my_function():
    print('I am a function.')

# Assign the function to a variable without parenthesis. We don't want to execute the function.
description = my_function
description()   

print("\n << eg 2 >> \n")
#======================================================================================================
#eg 2

def first(func):    ##passing the func as an argument
    def second():
        print("execute the first line")
        func() ##call the funct
        print("execute the second line")
    return second()

@first   ###decorate
def middle():
    print("execute the middle line")
 
# mid = first(middle)  ##another way to call decorate
middle

print("\n << eg 3 >> \n")
#======================================================================================================
#eg 3

def calculator(func):
    def operation(a,b):
        if a ==0 or b == 0:
            print("cannot calculate by zero")
        else:
            print("result :")
        return func(a,b)
    return operation

@calculator
def divide(a,b):
    print("division",a/b)

@calculator
def muiltiple(a,b):
    print("multiple",a*b)  
  
divide(5,10)
muiltiple(5,10)