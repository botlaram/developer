## create a simple class
class Book:
    
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
    def __str__(self) -> str:
        return self.author
        
b1=Book("nameofthebook","authorofbook")   #object 1
print(b1)

b2=Book("economic","dalal")               #object 2
print(b2)



