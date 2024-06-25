class Library:
    def __init__ (self):
        self.no_of_books=0
        self.books=[]
    def add_books(self,book):
        self.books.append(book)  
        self.no_of_books+=1  
    def print_books(self):
        print(f"The number of Book is {self.no_of_books}\nThe Books are {self.books}")
    
    

l1=Library()
l1.add_books("book1")
l1.print_books()
l1.add_books("book2")
l1.add_books("book3")
l1.add_books("book4")
l1.add_books("book5")
l1.print_books()

