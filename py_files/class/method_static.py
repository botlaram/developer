##class method :A class method is a method which is bound to the class and not the object of the class.
##static method : A static method is used when we want to create a function without using self as instance-(just to create a independent fucntin)
##ref : https://www.youtube.com/watch?v=16K7DvU5Bvw

class Employee:

    ##fix varaible 
    salary_amt=45000
    
    def __init__(self,name,emplyeid,incentive):
        self.name = name
        self.emplyeid = emplyeid
        self.incentive = incentive
        
    def __str__(self) -> str:
        return self.name
    
    ##classmethod is use to change the variable of class
    @classmethod
    def change_salary(cls,change_salary):   ##adding cls to access the variable of class (ie salary_amt)   
        cls.salary_amt=change_salary
    
    def totat_salary(self):
        total_Salary=Employee.salary_amt+self.incentive
        print(total_Salary ,"for ", self.name)
        
##call the class
ram=Employee("ram",451,45550)
Employee.change_salary(50000) ##change the salary_amt it will change for all objects

##creating other object
hari=Employee("hari",451,50000)

## after create a object for class , now call the function
ram.totat_salary()
hari.totat_salary()

print("\n << eg 2 >> \n")
#=============================================================================================================================
#eg 2
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a
	# Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a
	# Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

    ##static method eg 2
    ##this function is independent of the class ,created without using self as instance
	@staticmethod
	def thankyou(msg):
		return msg

person1 = Person('ram', 21)
person2 = Person.fromBirthYear('ram', 1997)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

# print thankyuu msg
print(Person.thankyou("thanks for looking up this file"))