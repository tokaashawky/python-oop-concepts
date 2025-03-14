class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.horsepower} HP {self.fuel_type} engine"

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def display_info(self):
        return f"- {self.year} {self.make} {self.model} with {self.engine}."

# Creating an Engine object
engine1 = Engine("petrol", 200)

# Creating a Car object with an Engine
car1 = Car("Toyota", "Camry", 2024, engine1)

# Testing functionality
print(car1.display_info())