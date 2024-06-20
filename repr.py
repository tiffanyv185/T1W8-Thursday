class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
    
     #creating an instance of book
    book1 = Book("1884", "George Orwell", 1984)

    # print repr to get the string representation
    print(repr(book1))
        
        