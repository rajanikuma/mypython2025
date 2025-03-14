class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print("-" * 20)  
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")
car4 = Car("BMW", "X5")
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()
