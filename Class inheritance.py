
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some animal sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

dog = Dog("Buddy")

print(dog.name)         
print(dog.make_sound())  
print(dog.fetch())       
