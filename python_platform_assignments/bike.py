class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed  
        self.miles = miles

    def displayInfo(self):
        print "bike costs " + str(self.price)
        print "the maximum speed is " + str(self.max_speed)
        print "the total miles is " + str(self.miles)

    def ride(self):
        self.miles += 10
        print "they see me rolling......" + str(self.miles)
    
    def reverse(self):
        self.miles -= 5
        print "woah woah woah, we going backwards mamma! " + str(self.miles)

bike_one = Bike(100, 20, 50)
bike_two = Bike(500, 30, 0)
bike_three = Bike(1000, 40, 100)

print bike_one.displayInfo()
print bike_one.ride()
print bike_one.reverse()