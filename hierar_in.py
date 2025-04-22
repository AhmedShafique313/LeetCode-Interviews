class Vehicle:
    def fuel(self):
        print("Uses fuel.")

class Car(Vehicle):
    def drive(self):
        print("Driving car.")

class Bike(Vehicle):
    def ride(self):
        print("Riding bike.")

obj1 = Car()
obj2 = Bike()

obj1.drive()
obj1.fuel()
obj2.ride()
obj2.fuel()