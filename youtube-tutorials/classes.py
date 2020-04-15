class Robot:
    def introduce_self(self):
        print('My name is {}'.format(self.name)) # this in Java

r1 = Robot()
r1.name = 'Tom'
r1.color = 'Red'
r1.weight = 30

r1.introduce_self()

r2 = Robot('Jerry', 'Blue', 40)

r2.introduce_self()