class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print('Welcome ', self.firstname, self.lastname, ' Year of Graduation: ', self.graduationyear)
    
x = student('Ahmed', 'Shafique', '2025')
x.welcome()