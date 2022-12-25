##multiple inheritance

class A:

    def __init__(self) -> None:
        super().__init__()  ##add super() to every class to fetch the values in mul. inheritnc
        self.foo = "foo"
        self.name="RAM"
      
class B:

    def __init__(self) -> None:
        super().__init__()
        self.bar = "bar"
        self.name="Krishna"  ##same var as name
      
class C(A,B):  ##adding multiple inheritance

    def __init__(self):
        super().__init__() ##add super() to every class to fetch the values in mul. inheritnc

 
    def getvalue(self):
        print(self.foo)
        print(self.bar)
        print(self.name)   ##fetch the class A name bcoz(A,B) A is called first

c=C()
c.getvalue()