class Library:
    def __init__(self,name, bookList, libraryName):
        self.name = name
        self.bookList = bookList
        self.libraryName = libraryName
        pass

    def addBook(self):
        return f"Your Name - {self.name}, Books are - {self.bookList}" \
               f" and Library Name is {self.libraryName}"

    def displayBook(self):
        return {self.bookList}

    def returnBook(self):
        print("Enter name of the book")
        book = input()
        return f"{book} successfully returned"

    def lendBook(self):
        print("Enter name of the book")
        book = input()
        return f"Sorry {book} is not available in our library"


i = 1
while (True):
    print("What do You want to do?")
    print("Press 1 for Add Book\n Press 2 for display list of the books\n"
          "Press 3 for Return book")
    inp = int(input())

    if inp == 1:
        print("Enter Your Name")
        name = input()
        print("Enter the list of the books")
        books = list(input())
        print("Enter library name")
        library = input()

        shanLibrary = Library(name, books, library)
        print("Books Added Successfully")
        print(shanLibrary.addBook())

    elif inp == 2:
        print("No books available")

    else:
        print("Enter the name of the book")
        retBook = input()
        print("Your Book is returned Successfully")

    i+=1



