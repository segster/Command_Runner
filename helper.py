def validate_and_execute(days_and_unit_dictionary):
    try:
    #if user_input.isdigit():
        user_input_num = int(days_and_unit_dictionary["days"])
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_num == 0:
            print ("urg hero to zero man")
        else:
            print ("u printed a negative number")
    except ValueError:
            print ("argggg NO TEXT ALLOWED!!")

def days_to_units(num_days,conversion_unit):
    if conversion_unit == "hours":
        return f"number of days is {num_days} which is {num_days * 24}  hours;"
    elif conversion_unit == "minutes":
        return f"number of days is {num_days} which is {num_days * 24 * 60}  minutes;"
    elif conversion_unit == "seconds":
        return f"number of days is {num_days} which is {num_days * 24 *60 * 60} seconds"
    else:
        return "unspported unit"
    #print (f"number of days is {num_days} which is {num_days * units}  hours;")
    print ("end")


