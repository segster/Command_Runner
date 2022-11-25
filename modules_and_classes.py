
#USER Base

class User:
    def __init__(self, email, name, password, current_job_title, login_attempts):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title
        self.login_attempts = login_attempts

    def change_pwd(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print (f"User {self.name} currently works as a {self.current_job_title}, you can contact them at {self.email}")

    def greet_user(self):
        print (f"Welcome {self.name} hope you enjoy the ride!")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print (f"{self.name}, you have attempted {self.login_attempts} logins ya looney !!")

    def reset_login_attempts(self, reset):
        if reset == 0 or reset == "reset":
            self.login_attempts = 0
            self.login_attempts = reset
            print (f"You reset the Login Attempts to {self.login_attempts}")

#######
#INHERITED CLASS


class Admin(User):
    """ A new admin class inherited from user class"""

    def __init__(self, email, name, password, current_job_title, login_attempts):
        """initilise attributes Of parent class"""
        super().__init__(email, name, password, current_job_title, login_attempts)
        #ADD CHILD CLASS
        self.privileges = Privileges()  #["can add post", "can delete post"]

    #def show_privileges(self):
    #    print (f"{self.name} has the following privileges:")
    #    for priv in self.privileges:
    #        print (priv)


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges1=[]):
        self.privileges1 = privileges1

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges1:
            for privilege in self.privileges1:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


doris_privileges = [
    'can reset passwords',
    'can stop discussions',
    'can suspend accounts',
    ]

doris = Admin('me.com', 'doris', 'brexit', 'PM', 0)
doris.privileges.privileges1 = doris_privileges

doris.privileges.show_privileges()


#print (doris)

doris.get_user_info()


#new_admin1.show_privileges


############################

class Pc_user:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.login_attempts  = int(0)


    def describe_user(self):
#        print(f"\nName = {self.first_name} {self.last_name}\nAge:{self.age}\nNationality {self.nationality}")
        details = f"\nName: {self.first_name.title()} {self.last_name.title()}\nAge: {self.age}\nNationality: {self.nationality.upper()}"
        return details


    def greet_user(self):
        print(f"Hello {self.first_name.title()} nice to see you")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#################################

class L2_untrusted:
    def __init__(self):
        self.vlan = input("\nEnter VLAN\n")
        self.vni =  input ("\nEnter VNI\n")
        self.site = input ("\nEnter site\n")
        self.edge_device = input("\nEnter Edge CLE devoice\n")
        self.description = input("\nEnter description\n")
        self.freeform_text = input ("\nEnter Freeform Text\n")

    def display_details(self):
        print (f"Your details are as follows:\nVLAN {self.vlan}")
        print(f"VNI {self.vni}")
        print(f"SITE {self.site}")
        print(f"Edge Device {self.edge_device}")
        print(f"Description {self.description}")
        print(f"Freeform Text {self.freeform_text}\n")
        #print ("end")



##CRASH Course STUFF#################

class Dog:
    """
    An attempt at making a class of dog
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print (f"{self.name} is now sitting")

    def rollover(self):
        print (f"{self.name} rolled over")

######################################


#############################################

class Restaurant:
    def __init__(self, rname, cuisine):
        self.rname = rname
        self.cuisine = cuisine
        self.cust_served = 0

    def describe_restaurant(self):
        print (f"This restauarant is called {self.rname} and is serves {self.cuisine}")

    def is_open(self):
        print (f"{self.rname} is now open")

    def customers_served(self):
        print (f"{self.rname} has served {self.cust_served} customers")

    def set_number_served(self, served):
        self.cust_served = served

    def increment_number_served(self, cserved):
        self.cust_served += cserved

class IceCreamStand(Restaurant):
    """ Excercise 9.6 page 173"""

    def __init__(self, rname, cuisine):
        super().__init__(rname, cuisine)
        self.flavours = ['peach', 'vanilla']

    def list_flavours(self):
        print(f"{self.rname} has the following flaours:")
        for flav in self.flavours:
            print(flav)

stand1 = IceCreamStand("Giorgo", "Ices")
#print (stand1)

stand1.list_flavours()



#######









def count(start=0, increment=1):
    while True:
        start += increment
        print(start)

#
#count(0,1)




