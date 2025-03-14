

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"
def make_sound(animal):
    print(animal.sound())
dog = Dog()
cat = Cat()
make_sound(dog)  
make_sound(cat)  
