class student:
    def __init__(self, fname, lname, year):
        self.firstname = fname
        self.lastname = lname
        self.graduationyear = year
    
    def welcome(self):
        print('Welcome ', self.firstname, self.lastname, ' Year of Graduation ', self.graduationyear)

x = student('Ahmed', 'Shafique', '2025')
x.welcome()