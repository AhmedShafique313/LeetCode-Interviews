class animal:
    def sound(self):
        print('Dog is an animal')

class dog(animal):
    def bark(self):
        print('Dog Bark')

obj = dog()
obj.sound()
obj.bark()