from modules_and_classes import Dog
from modules_and_classes import Car
from modules_and_classes import Pc_user

my_dog = Dog("willie", 6)

print (f"my dogs name is {my_dog.name}")

print (f"my dog, {my_dog.name} is {my_dog.age}")

my_dog.sit()
my_dog.rollover()

your_dog = Dog("dave", 16)

print (f"my dogs name is {your_dog.name}")

print (f"my dog, {your_dog.name} is {your_dog.age}")


 ###car

my_new_car = Car("Porsche", "911", 2022)
print (my_new_car.get_descriptive_name())
my_new_car.mileage_reading = 70
my_new_car.read_mileage()


my_new_car2 = Car("Ferrari", "Daytona", 2022)
print (my_new_car2.get_descriptive_name())


my_new_car2.update_mileage(10)
my_new_car2.read_mileage()

my_new_car2.increment_mileage(8000)
my_new_car2.read_mileage()

greet1 = Pc_user("simon", "edmonds", 59, "uk")
print (greet1.describe_user())

greet1.greet_user()

greet2 = Pc_user("harry", "edmonds", 11, "uk")
print (greet2.describe_user())

greet2.greet_user()

greet3 = Pc_user("george", "edmonds", "13", "italy")
print (greet3.describe_user())

greet3.increment_login_attempts()
greet3.increment_login_attempts()
greet3.increment_login_attempts()
greet3.reset_login_attempts()

print(greet3.login_attempts)