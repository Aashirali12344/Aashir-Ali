class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("The name is ",self.name)
        print("The age is ",self.age)

class Employee(person):
    def __init__(self,name,age,empid):
        self.empid=empid
        person.__init__(self,name,age)
    def display(self):
        super().display()
        pritn("the empid is",self.empid)

ali=Employee("Ali",20,123)
ali.display()        


class person1:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printName():
        print("the full name is ", self.fname,self.lname)
class student(person1):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
std=student("Ali","Khan",2024)
std.printName()
print("the graduation year is",std.graduationyear)

class Animal:
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run") 
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("i can roar")


h=Human()
h.move()
s=Snake()
s.move()
d=Dog()
d.move()
l=lion()
l.move()

