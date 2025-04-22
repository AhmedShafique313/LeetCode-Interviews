from abc import ABC, abstractmethod

class base_class(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print('Speed up...')
    
    def braking(self):
        print('Car Stopped...')
    
class hatchback(base_class):
    def printDetails(self):
        print('Brand: ', self.brand)
        print('Model: ', self.model)
        print('Year: ', self.year)
    
    def sunroof(self):
        print('This feature is not included in this car')

class suv(base_class):
    def printDetails(self):
        print('Brand: ', self.brand)
        print('Model: ', self.model)
        print('Year: ', self.year)
    
    def sunroof(self):
        print('The car has a sunroof')

car1 = suv('BMW', 'M3', '2022')
car1.printDetails()
car1.accelerate()
car1.sunroof()