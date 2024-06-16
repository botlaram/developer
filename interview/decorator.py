#decorator

def my_decorator(func):
    def wrapper():
        print("before func execution")
        func()
        print("after func execution")
    return wrapper

@my_decorator
def do_that(): 
    print("do that...")
    
@my_decorator
def do_this():
    print("do this...")
    
do_that()
do_this()
