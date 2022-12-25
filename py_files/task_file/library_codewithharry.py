##mini project 
##library project (code with harry)
##display book
##lend book
##add book
##return book
##link - https://www.youtube.com/watch?v=hyZA885xVmc&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=102

class Library:
    
    def __init__(self,*list_book):
        self.list_book=list(list_book)
        
    ##display book
    def display_book(self):
        print(" available books in library: \n" ,self.list_book)

    ##lend book taking book
    
    def lend_book(self):
        self.dict_lend_book = {}
        for i in range(1):
            name=input("enter your name to lend book: \n")
            need_book=input("Enter the book you want \n")
            self.dict_lend_book[name]=need_book
        for need_book in self.list_book:
            self.list_book.remove(need_book)
        print("books lend to : \n",self.dict_lend_book)
        print("total books available in library: \n" ,self.list_book)
         
    ##add book
    def add_book(self):
        self.dict_donate_book = []
        for i in range(1):
            donate_book=input("Enter the book you want to donate \n")
            self.dict_donate_book.append(donate_book)
            self.list_book.append(donate_book)
        print("thanks for donating the book: \n" ,self.dict_donate_book)
        print("total books available in library: \n" ,self.list_book)
        
    ##return book
    def return_book(self):
        self.return_book_name = []
        for i in range(1):
            book_to_return=input("enter the book to return:\n ")
            self.return_book_name.append(book_to_return)
        for i in self.return_book_name:
            if i not in self.list_book:
                self.list_book.append(i)
        print("thanks for returning the book: \n",self.return_book_name)
        print("total books available in library: \n" ,self.list_book)
        

vrec_library=Library("peace","spirit")
vrec_library.display_book()
vrec_library.lend_book()
vrec_library.add_book()
vrec_library.return_book()

#######code with harry scripts #####
print("\n code with harry scripts \n")


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")

    while(True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue