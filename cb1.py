
import helper
#import paramiko
#import netmiko
import os

#from helper import validate_and_execute
#from helper import *
#import helper as h

user_input = ""
while user_input != "exit":
     user_input = input("Hey user enter number of days and conversion unit\n")
     user_input = user_input.lower()
     if user_input == "exit":
         print ("EXITING PROGRAM")
         break
     days_and_units = user_input.split(":")
     print (days_and_units)
   # for num_of_days_element in user_input.split():
    #    validate_and_execute()
    #print (days_and_units)
     days_and_unit_dictionary = {"days": days_and_units[0], "unit":days_and_units[1]}
    #print (days_and_unit_dictionary)
     helper.validate_and_execute(days_and_unit_dictionary)


print (os.name)