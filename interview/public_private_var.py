#all members in python as default public

##public class example

class Student:

    schoolName="XYZ school (public key)" #class attribute

    def __init__(self,name,age):
        self.name=name
        self.age=age        #instance attribute

std1=Student("ram",25)

std1.schoolName="ABC school"  #updated school name
print(std1.schoolName)

##Protected Members
#Protected members of a class are accessible from within the class and are also available to its sub-classes. 
#No other environment is permitted access to it. 
#This enables specific resources of the parent class to be inherited by the child class.


class Employee:
    
    __org="ZF Tech (private key)" # protected class attribute
    
    def __init__(self,name,id) -> None:
        self._name=Employee.__org  #assign private key
        self._id=id  # protected instance attribute
        
    def accesswithinclass(self):
        print(Employee.__org)
        
emp=Employee("RAMA",5502209)
emp.accesswithinclass()
print(emp._name)
print(emp.__org)   #cannot access here private key
