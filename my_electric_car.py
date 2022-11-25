from car import ElectricCar

my_tesla = ElectricCar('tesla', 's', 2022)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
#
#removed configuration for below
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()