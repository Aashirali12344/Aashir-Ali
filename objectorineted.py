class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(self.name)
        print(self.id)

    def __del__(self):
        print("destructor function called")

obj_emp = employee("Aashir", 1234)
obj_emp.show()
del obj_emp


class library:
    def __init__(self,list1,name):
        self.booklist=list1
        self.name=name
        self.lenddict={}
    def display(self):
        print("we have the list of books as followed")
        for book in self.booklist:
            print(book)
def lendabook(self,user,book):
    if book not in self.lenddict.keys():
        self.lenddict.update({book:user})
        print("the book is assigned to the user")

    else:
        print("the book is already assigned to the user")
def addbook(self,book):
    self.booklist.append(book)
    print("book is added")

def returnbook(self,book):
    if book in self.lenddict:
        self.lenddict.pop(book)
        print("book returned successfully")
    else:
        print("This book was not lent out.")
    
book=library(["python","c#","ASP","PHP","REACT","Angular","SQL","Javascript"],"codingal")
while(True):
    print("1.display book")
    print("2.lend book")
    print("3.add book")
    print("4.return book")
user_choice=int(input("Enter your choice"))

if user_choice==1:
    book.display()
elif user_choice==2:
    name=int(input("enter your name"))
    bookname=input("enter the book name")
    book.lendabook(name,bookname)
elif user_choice==3:
    bookname=input("enter the book you want return")
    book.returnbook(bookname)
else:
    print("enter a valid choice")
print("press 'q' to quit or 'c' to continue")


user_choice= ""
while(user_choice!="q" and user_choice!="c"):
    user_choice=input()
    if user_choice=="q":
        exit()
    elif user_choice=="c":
        continue





print(self.booklist)
print(self.name)
        