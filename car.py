"""A class that can be used to represent a car"""
from pip._internal.commands.show import print_results


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage_reading  = 1000

    def read_mileage(self):
        print (f"This car has {self.mileage_reading} miles on it")

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model}  {self.year}"
        return long_name.title()

    def update_mileage(self, mileage):
        if mileage >= self.mileage_reading:
            self.mileage_reading = mileage
        else:
            print (f"you crook, you rolled back the reading on the {self.model}")

    def increment_mileage(self, miles):
        self.mileage_reading += miles

class Battery:
    """A simple attempt to model a Battery for an elecric car Class"""

    def __init__(self, battery_size=75):
        """initialise the batterys attributes"""
        self.battery_size = battery_size


    def describe_battery(self):
        """print a statement about the battery size"""
        print (f"This car has a {self.battery_size}--Kwh battery")

    #def battery_range(self):
    #    """print statement about battery range"""
    #    print (f"This battery has a range of {self.range} miles ")

    def get_range(self):
        """"print a statement about the battery range"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")




class ElectricCar(Car):
    """Represents aspects of an Electric car"""

    def __init__(self, make, model, year):
        """"initialise attributes of the parent class"""
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery = Battery()


    def describe_battery(self):
        """A print statement describimng battery size"""
        print (f"This car has a {self.battery_size}-Khw battery.")




