class Restaurent:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("The name of the restaurent is "+self.restaurant_name+" and customer served "+ str(self.number_served))
    def open_restaurant(self):
       print("The restaurent is open")
    def update_number_served(self,num_served):
        self.number_served=num_served
class IceCreamStand(Restaurent):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def describe_flavor(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print('\t'+flavor)

r1=Restaurent('Pizza Hut','Pizza')
print("Number of customer served "+str(r1.number_served))
i1=IceCreamStand('Abeers stand','Ice','vanilla','chocolate','butter scotch')
i1.describe_flavor()
r1.update_number_served(10)
r1.describe_restaurant()
r1.open_restaurant()