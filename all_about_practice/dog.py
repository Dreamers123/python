class Pet():
 def __init__(self,name,age):
     self.name=name
     self.age=age
     self.color='Green'
     self.hunt=True
 def sit(self):
     print(self.name.title() +" is now sitting ")
 def roll(self):
     print(self.name.title() +" rolled over just now")
 def describe(self):
     print("The name of my dog is "+ my_dog.name.title()+" and age is "+str(self.age))
 def update_color(self,new_color):
     self.color=new_color
 def update_age(self,new_age):
     if new_age>=self.age:
        self.age=new_age
     else:
         print("You can't do that")

class Weight():
     def __init__(self,weight=40):
         self.weight=weight
     def describe_weight(self):
        print("My dog is "+str(self.weight)+" pounds in weight")
     def runnig_ability(self):
         if(self.weight) ==30:
             strength=45
             ##print("It can run at " +str(strength)+" KM per hour")
         elif(self.weight)==40:
             strength=50
             print("It can run at " +str(strength)+" KM per hour")
         else:
             print("Haven't test it before")

class Dog(Pet):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.weight=Weight()
        self.hunt=True

    def can_hunt(self):
        if(self.hunt == True):
         print("Yeh,it's ahunting Dog")
        else:
         print("No,it's not a hunting dog")




my_dog=Dog('Doggie',7)
print("The name of my dog is "+ my_dog.name.title()+" and color is "+my_dog.color)
my_dog.describe()
my_dog.roll()
my_dog.update_color('Drak')
print("The name of my dog is "+ my_dog.name.title()+" and color is "+my_dog.color)
my_dog.update_age(9)
my_dog.describe()
my_dog.weight.describe_weight()
my_dog.weight.runnig_ability()
my_dog.can_hunt()



