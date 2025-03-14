
print (" rajani 60")
class MyClass:
    class_variable = 10  

    @classmethod
    def class_method(cls):
        print(f"Class method: class_variable = {cls.class_variable}")

    @staticmethod
    def static_method():
        print("Static method: No class or instance needed!")
MyClass.class_method()  
MyClass.static_method()  
