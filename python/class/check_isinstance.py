class Book:

    def __init__(self,title) -> None:
        self.title = title

class Newspaper:

    def __init__(self,name) -> None:
        self.name = name

      
b1=Book("this is b1 title")
b2=Book("this is b2 title")

n1=Newspaper("this is n1 newspaper")
n2=Newspaper("this is n2 newspaper")

##check instance of the specific class
print(type(b1) == type(b2))
print(type(b1) == type(n2))

 

##using isinstance to check the instance of the specific class

print(isinstance(b1,Book))
print(isinstance(n2,Book))

print(isinstance(n2,object))