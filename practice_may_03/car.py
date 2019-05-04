class Car():
    def __init__(self,manufacturer, model, year):
        self.manufacturer=manufacturer
        self.model=model
        self.year=year
        self.otometer=60

    def increment_odometer(self, miles):
        self.otometer += miles
class Battery():
    def __init__(self,size,range=40):
        self.size=size
        self.range=range
    def get_range(self):
        if self.size>60:
           self.range=120
        else:
            self.range=90
        message = "This car can go approximately " + str(self.range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    def __init__(self, manufacturer, model,year):
        super().__init__(manufacturer, model, year)
        self.mileage=80
        self.battery=Battery(80)
    def set_mileage(self,mileage):
        if self.battery.size<mileage:
            self.mileage=mileage
        else:
            print("You can't set that to " +str(mileage))

car_1=ElectricCar("Tesla","Vintage",2019)
#car_1.set_mileage(30)
print(car_1.battery.get_range())