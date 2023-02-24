
class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("[Insert Animal Noise Here...]")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
class Other_Pet(Pet):
    def __init__(self, type, name, age):
        super().__init__(name, age)
        self.type = type
    def show(self):
        print(f"I am a {self.type}, my name is {self.name} and I am {self.age} years old")


class Cat(Pet):
    def speak(self) :
        print( "Meow" )

class Dog(Pet):
    def speak(self) :
        print( "Bark" )


s= Other_Pet("Snake", "Slippy", 53)
s.show()
s.speak()
p= Pet("Tim", 19)
p.show()
p.speak()
c = Cat("Jared", 22)
c.show()
c.speak()
d = Dog("Stelly", 2)
d.show()
d.speak()