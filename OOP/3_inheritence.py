class Vehicle:
    def __init__(self, v_type, color, mileage):
        self.v_type = v_type
        self.color = color
        self.mileage = mileage

# Derived class
class Car(Vehicle):
    def display(self):
        print("Vehicle Type:", self.v_type)
        print("Color:", self.color)
        print("Mileage:", self.mileage)

# Object
c1 = Car("Car", "Red", 20)
c1.display()
