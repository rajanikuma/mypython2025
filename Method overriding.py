print ( "Rajani 60")

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
animal = Animal()
animal.make_sound()  

dog = Dog()
dog.make_sound()  
