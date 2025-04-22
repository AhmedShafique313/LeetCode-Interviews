class chef:
    def cook(self):
        print('Robot is a chef')

class robot:
    def move(self):
        print('Robot can move')

class RobotChef(chef, robot):
    pass

obj = RobotChef()
obj.cook()
obj.move()