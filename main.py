class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old ")
    def make_sound(self):
        print("the sound of cat is meow")
class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a bird. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("the sound of a bird is tweet")

c1=cat("tom",2)
c1.info()
c1.make_sound()

b1=bird("parrot",3)
b1.info()
b1.make_sound()

class sparrow(bird):
    def __init__(self, name, age):
        super().__init__(name, age)
    def info(self):
        print(f"I am a Sparrow , My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("The sound of sparrow is chirp")

s1=sparrow("Sparrow",4)
s1.info()
s1.make_sound()

for animal in (c1,b1,s1):
    animal.make_sound()
    animal.info


class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        self.__maxprice=900
    def sell(self):
        print("Selling price: {}".format(self.maxprice))
    def setMaxPrice(self,price):
        self.__maxprice=price

c=computer("i5",16)
c.sell()
c.__maxprice=1000
c.sell()
c.setMaxPrice(1000)
c.sell()