class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
    
    def display_all(self):
        print "the car costs " + str(self.price) + ", it's speed is " + str(self.speed) + ", it has " + str(self.fuel) + " gallons of gas in the tank, and the milage is " + str(self.milage) + ", the tax rate on this bad boy is " + str(self.tax)
    
expensive_car = Car (15000, 160, 15, 30000)
expensive_car.display_all()

cheap_honda = Car (3000, 90, 10, 200000)
cheap_acura = Car (2000, 100, 11, 250000)
decent_nissan = Car (11000, 140, 13, 20000)
decent_scion = Car (14000, 150, 10, 40000)
expensive_gtr = Car (100000, 170, 12, 45000)

cheap_honda.display_all()
cheap_acura.display_all()
decent_nissan.display_all()
expensive_gtr.display_all()