class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self): # polymorphism a same name function
        print('Drive')

class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self): # polymorphism a same name function
        print('Sail')

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self): # polymorphism a same name function
        print('Fly')

car1 = car("Ford", "Mustang")       #Create a Car object
boat1 = boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
    x.move()