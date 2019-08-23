class Animal:
    def __init__(self):
        print ("animaw created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

# a = Animal()

# a.eat()

class Dog(Animal):
    def __init__(self):
        print("Dog created")

    def who_am_i(self):
        print("I am Dog")

    def eat(self):
        print("dog is  eating")


# my_dog = Dog()
# my_dog.eat()


#------------------------Polymorphism----------------------------------------------
class Toad():
    
    def __init__(self,name):
        self.name = name
        print (name + "<--constructor called--")

    def speak(self):
        return (" toad is Speaking")




class cat():
    def __init__(self, name):
        self.name = name
        print(name + "   Cat construc cALLed")

    def speak(self):
        return (self.name," is speaking")


Toby = Toad("rob")
Toby.speak()

grav = cat("grav")
grav.speak()

for i in [Toby, grav]:
    print(i.speak(), "<--")