'''public, protected and private access modifiers'''

# protected can be assigned by single (_)

class Student:
    
    #protected vars
    _name=None
    _roll=None
    _branch=None
    
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
        
    # protected function
    def _displayrollandbranch(self):
        print(f"Roll No: {self._roll} and Branch: {self._branch}")
        
        
# inheritance

class School(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
        
    def display_all_var(self):
        print(self._name)  #protected var of Student class
        
        self._displayrollandbranch() #call protect function of student class
      
      
obj=School("Rama","8","CSE")
obj.display_all_var()



# private

