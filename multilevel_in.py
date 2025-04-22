class grandfather:
    def lagecy(self):
        print('Lagecy pass down')

class father(grandfather):
    def skills(self):
        print('father skills')

class son(father):
    def playing(self):
        print('son is playing')

obj = son()
obj.lagecy()
obj.skills()
obj.playing()