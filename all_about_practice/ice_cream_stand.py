class Restaurant():

 def __init__(self,name,cuisine_type):
     self.name=name
     ##self.brand=brand
     self.cuisine_type=cuisine_type
class Ice_cream_stand(Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavors = []
    def describe_flavor(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print("- "+flavor)
    def describe_stand(self):
        print("The name of the stand is "+self.name+",stand type "+self.cuisine_type)
my_stand=Ice_cream_stand("Abeer's stand",'Ice_cream')
my_stand.describe_stand()
my_stand.flavors=['venilla','chocolate','butter scotch']
my_stand.describe_flavor()