class person:
    def info(self):
        print('I am a person')

class teacher(person):
    def teach(self):
        print('Teach the students')

class sportsman(person):
    def sports(self):
        print('I play sports')

class schoolStaff(teacher, sportsman):
    def duty(self):
        print('I am a part of school staff')

obj = schoolStaff()
obj.info()
obj.teach()
obj.sports()
obj.duty()