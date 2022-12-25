#basic class structure
##eg 1

class Student:
    ##self hold the value of instant obj
    def __init__(self,name,age) -> None:   ##here self represent to b1
        self.name = name
        self.age = age
           
    def __str__(self) -> str:   ##__str__() function controls what should be returned when the class object is represented as a string.
        return f"{self.name}"
   
    def hello(self):  ## funct is called methods in class
        print("heellooo")

    def get_name(self):
        return self.name

    def get_details(self):
        print("name",self.name)
        print("age",self.age)

##for every class we need to define obj
##here b1 var is obj for class Book
b1 = Student("RAM",26)  ##b1 here is obj
b1.hello()   ##obj.method
print(b1.get_name())    ##obj.method
b1.get_details()


b2=Student("Krishna",11)
b2.get_details()

print("\n << eg 2 >> \n")
#=============================================================================================================================
#eg 2

class Book:
    def __init__(self,title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.__secret = 'this is secret value'   ##doubleunderscore are hidden var of other class

  
    def get_title(self):  ##get title of book
        return self.title
 
    def get_price(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price*self._discount)
        else:
            return self.price
   
    def setdiscount(self,amount):
        self._discount = amount     ##singleunderscore var is access only for internal class
           
b1=Book("PeaceofMind","Unknown",100)
print(b1.get_title())
print("price before discount",b1.get_price())

b1.setdiscount(0.5)
print("price after discount",b1.get_price())

print(b1._Book__secret)    ##to print secret value used in class (obj._class__<sec_name>)
