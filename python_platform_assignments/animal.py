class Animal (object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk (self):
        self.health -= 1
    def run (self):
        self.health -= 5
    def display (self):
        print str(self.health)
good_boy_1 = Animal ("clifford", 100)
good_boy_1.run()
good_boy_1.display()

class Dog (Animal):
    def __init__(self):
        self.health = 150
    def pet (self):
        self.health += 5

paul = Dog ()
paul.health = 10
paul.pet()
paul.run()
paul.display()

class Dragon (Animal):
    def __init__(self):
        self.health = 170

    def fly (self):
        self.health -= 10
    
    def display_health(self):
        Animal.display(self.health)
        print "I am a dragon"
dacarius = Dragon ()
dacarius.health = 13000
dacarius.fly()
dacarius.fly()
dacarius.fly()
dacarius.display()