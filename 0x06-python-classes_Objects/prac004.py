#!/usr/bin/python3
class robot:
    population = 0;

    def __init__(self, name):
        self.name = name;
        print("(Initializing {})".format(self.name))

        robot.population += 1

    def die(self):
         print("{} is being destroyed!".format(self.name))
         robot.population -= 1

         if robot.population == 0:
            print("{} is being destroyed!!".format(self.name))
         else:
            print("There are {:d} robots working".format(robot.population))

    def say_hi(self):
        print("Greetings, masters. Call me {}.".format(self.name))
    
    @classmethod

    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))

a=robot("R2-D2")
a.say_hi()
robot.how_many()

b=robot("C-3PO")
b.say_hi()
robot.how_many()

print("\nRobot can do some work here\n")

print("Robots have finished their work. So let's destroy them.")

a.die()
b.die()


robot.how_many()