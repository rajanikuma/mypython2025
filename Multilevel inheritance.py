
class Animal:
    def sound(self):
        print("Animals make sounds.")
class Mammal(Animal):
    def feed_milk(self):
        print("Mammals feed milk to their babies.")
class Dog(Mammal):
    def bark(self):
        print("Dogs bark.")
dog = Dog()
dog.sound()      
dog.feed_milk() 
dog.bark()       
