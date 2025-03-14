print (" rajani 60")

class Parent:
    def show_message(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show_message(self):
        super().show_message() 
        print("This is the Child class method.")
obj = Child()
obj.show_message()
