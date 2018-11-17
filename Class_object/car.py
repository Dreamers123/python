class Car():

 def __init__(self,name, make, model, year):
  self.name = name
  self.make = make
  self.model = model
  self.year = year
  self.odometer_reading = 0
 def roll_over(self):
  print(self.name.title() + " rolled over!")
 def update_odometer(self, mileage):
   if mileage >= self.odometer_reading:
    self.odometer_reading = mileage
   else:
    print("You can't roll back an odometer!")
 def read_odometer(self):
  print("This car has " + str(self.odometer_reading) + " miles on it.")
 def get_descriptive_name(self):

  long_name = str(self.year) + ' ' + self.make + ' ' + self.model
  return long_name.title()
class Battery():
 def __init__(self, battery_size=70):
  self.battery_size = battery_size
 def get_range(self):
  if self.battery_size == 70:
    range = 240
  elif self.battery_size == 85:
    range = 270

  message = "This car can go approximately " + str(range)
  message += " miles on a full charge."
  print(message)
 def describe_battery(self):
  print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
 def __init__(self,name,make, model, year):
  super(ElectricCar, self).__init__(name,make, model, year)

  self.battery = Battery()
 def gasTank(self):
  print("No gas")

my_new_Ecar=ElectricCar('volkswagen','Audi','Tesla',2020)
my_new_Ecar.battery.get_range()
my_new_Ecar.gasTank()
my_new_car = Car('Black beast','audi', 'a4', 2016)
my_new_car.update_odometer(239)
my_new_car.odometer_reading=30
my_new_car.read_odometer()
print(my_new_car.get_descriptive_name())
my_new_car.roll_over();