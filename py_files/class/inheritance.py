##without inheritance
 
class Book:

    def __init__(self,title,author,pages,price) -> None:
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price

 
class Magazine:

    def __init__(self,title,publisher,pages,price) -> None:   ##using the title,pages repeated var
        self.title=title
        self.publisher=publisher
        self.pages=pages
        self.period=price
   
class Newspaper:

    def __init__(self,title,publisher,pages,price) -> None:
        self.title=title
        self.publisher=publisher
        self.pages=pages
        self.period=price

book=Book("PeaceofMind","Unknown",100,50.50)

mag=Magazine("Vogue","Kiran",20,15)

news=Newspaper("TOI","toi",5,3)

print(book.title)

print(mag.publisher)

 
#====================================================================================
print("\n\nwith inheritance \n\n")

class Publisher:

    def __init__(self,title,price) -> None:
        self.title=title
        self.price=price
 
class Author(Publisher):   ##add class name to inherit

    def __init__(self,title,price,pages,period) -> None:
        super().__init__(title,price)   ###add module super()to fetch the var for Publisher class
        self.period=period
        self.pages=pages
  
class Book1(Publisher):    ##add class name to inherit

    def __init__(self,title,price,author) -> None:
        super().__init__(title,price)
        self.author=author    ##adding variable rather then class
      
class Magazine1(Author):

    def __init__(self,title,author,pages,period) -> None:   ##using Author class to fetch the values
        super().__init__(title,author,pages,period)
      
class Newspaper1(Author):

    def __init__(self,title,price,pages,period) -> None:
        super().__init__(title,price,pages,period)

      
b1=Book1("PeaceofMind","Unknown",100)

m1=Magazine1("Vogue","Kiran",20,15)

n1=Newspaper1("TOI","toi",5,10)

print(b1.author)

print(m1.period)
