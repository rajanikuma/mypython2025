

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Used for a user-friendly string representation (e.g., when using print())."""
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        """Used for an official string representation (useful for debugging)."""
        return f"Person('{self.name}', {self.age})"
p = Person("Alice", 30)
print(str(p))  
print(repr(p))  
