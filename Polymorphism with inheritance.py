
class Animal:
    def sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
def make_sound(animal):
    print(animal.sound())
dog = Dog()
cat = Cat()
animal = Animal()
make_sound(dog)    
make_sound(cat)    
make_sound(animal) 
