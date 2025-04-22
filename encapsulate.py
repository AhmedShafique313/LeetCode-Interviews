class private:
    def __init__(self):
        self._age = 30

class public(private):
    def display_age(self):
        print(self._age)

obj = public()
obj.display_age()