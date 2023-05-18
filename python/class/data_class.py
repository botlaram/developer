##without dataclass

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person=Person("Ram","krishna",26)
print(person.first_name)


##with dataclass
from dataclasses import dataclass,field

@dataclass
class Book:
    title : str
    author : str
    price : float
   
book=Book("Peaceofmind","Unknown",50.50)
print(book.price)

 
print("\n << eg 2 >> \n")
#=============================================================================================================================
#eg 2

##dataclass with default values

@dataclass
class Default:

    name:str = "Hari"
    employeid:int=field(default=123456)  ###field is use to set default value for all objects

default=Default() ###calling class without passing arguments
pass_values=Default("krishna") ##passing only one parameter

print(default)
print(default.name)
print(pass_values)
