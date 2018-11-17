
class Vehicle:
   def __init__(self,name,type,milage):
        self.name = name
        self.type = type
        self.milage=milage
   def __str__(self):
        return self.name +",with "+str(self.milage)+" milage transport type vehicle "
   def add_extra_info(self,**vehicle_info):
      vehicle = {}
      for key, value in vehicle_info.items():
          vehicle[key] = value
      return vehicle

class Truck(Vehicle):
      vehicle={}
      def __init__(self, name,type,milage,weight_capacity,**vehicle_info):
        super().__init__(name, type,milage)
        self.weight_capacity = weight_capacity
        for key,value in vehicle_info.items():
            self.vehicle[key]=value
      def increase_milage(self,mile):
          self.milage=mile

      def describe_vehicle(self):
           for key,value in self.vehicle.items():
               print(self.vehicle)
           else:
               print(self.name)

      def __str__(self):
        return super().__str__() +" with "+str(self.weight_capacity)+" ton capacity "

class Bus(Vehicle):
      def __init__(self, name,type,milage,passenger_capacity):
        super().__init__(name, type,milage)
        self.passenger_capacity = passenger_capacity
      def __str__(self):
        return super().__str__() +" with "+str(self.passenger_capacity)+" passenger capacity"

v1=Truck('Truck','public',120,100,company='princeton')
v2=Bus('Bus','public',200,200)

v1.increase_milage(140)
print(v1.add_extra_info(company='princeton'))
print(v1.describe_vehicle())
print(v2)