try:
    a=b
except:
    print("this is an error")   ##sent added by over end

print("\n << eg 2 >> \n")
#======================================================================================================
#eg 2

try:
    x=10
    y="str"
    z=x+y
except NameError:                      ##cannot add the Namerror exception at end because it is child class
    print("please define the var")
except Exception as ex:
    print("error >",ex)
  
print("\n << eg 3 >> \n")
#======================================================================================================
#eg 3

try:
    x=10
    y="str"
    z=x+y
    print(z)
except NameError:                      ##cannot add the exception at end because it is child class
    print("please define the var")
except TypeError:
    print("cannot concatenate int with str")
except Exception as ex:                   ##exception is return at last
    print("error > ",ex)

print("\n << eg 4 try except and else, finally >> \n")
#======================================================================================================
#eg 4 try except and else, finally

try:
    x=int(input("enter the value"))
    y=int(input("enter the value"))
    z=x+y
except NameError:                      ##cannot add the exception at end because it is child class
    print("please define the var")
except ValueError:
    print("please enter the integer value")
except Exception as ex:                   ##exception is return at last
    print("error > ",ex)
else:
    print(z)
finally:    ##even there s error in code this will execute
    print("execution is done")

    
print("\n << eg 5 raise exception >> \n")
#======================================================================================================
#eg 5 raise exception

 
a=input("wht is your name > ")
b=input("enter the input > ")
 
if a.isnumeric():
    raise Exception("please enter the str input")  ##modify the exception
if int(b) == 0:
    raise ZeroDivisionError("cannot divide by zero")
print(f"hello {a}")