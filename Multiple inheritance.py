print (" rajani 60")
class Parent1:
    def func1(self):
        print("This is function 1 from Parent1.")
class Parent2:
    def func2(self):
        print("This is function 2 from Parent2.")
class Child(Parent1, Parent2):
    def func3(self):
        print("This is function 3 from Child.")
child_obj = Child()
child_obj.func1()  
child_obj.func2() 
child_obj.func3()  
