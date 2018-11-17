class resturent():

 def __init__(self, name, brand ,color, prize):
     self.name=name
     self.brand=brand
     self.color=color
     self.prize=prize

 def describe_ice(self):
     print("The name of the ice-cream is" +" "+ self.name.title())
class Flovar():
    def __init__(self,flavor="Butter Scotch"):
        self.flavor=flavor
    def flavorIs(self):
        print("The flavor is"+" "+str(self.flavor))
class IceCreamStand(resturent):
 def __init__(self, name,brand, color, prize):
  super(IceCreamStand, self).__init__(name,brand, color, prize)
  self.flavor=Flovar()



Mystand=resturent('cone','igloo','white',200)
NewStand=IceCreamStand('Scoop','Bloop','Creamy',250)
NewStand.describe_ice()
NewStand.flavor.flavorIs()


