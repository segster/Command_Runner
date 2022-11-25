#from car import Car, ElectricCar

import car

from car import *


my_new_car = car.Car('audi', 'a6', 2019)
print (my_new_car.get_descriptive_name())

my_new_car.mileage_reading = 7000
my_new_car.read_mileage()


my_tesla = ElectricCar('tesla', 's', 2022)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
#
#removed configuration for below
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()