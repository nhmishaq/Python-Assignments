class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    
    def sell_product(self):
        self.status = "sold"
    
    def add_tax(self, tax):
        self.price += tax
        return self.price
    
    def return_item (self, reason):
        if (reason == "defective"):
            self.status = "defective"
            self.price = 0
        elif (reason == "return brand new"):
            self.status = "like new"
            self.price -= (0.2*self.price) 
        else: 
            self.status = "for sale"
    def display_info(self):
        print "Price: " + str(self.price) + ", Item Name: " + str(self.item_name) + ", Item Wright: " + str(self.weight) + ", Item Brand: " + str(self.brand) + ", Item Cost: $" + str(self.cost) + ", Item Status: " + str(self.status)

under_armuor_shirt = Product (49, "Under Armuor Shirt", 1, "Under Armour", 15, "for sale")
under_armuor_shirt.return_item("defective")
under_armuor_shirt.display_info()