
from datetime import datetime

user_input = input ("enter your goal with a deadline seperated by colon\n")

user_input_date = input ("Enter date in dd.mm.yyyy style\n")


input_list = user_input +":" + user_input_date
input_list = input_list.split(":")
print (input_list)

goal = input_list[0]
deadline = input_list[1]
deadline_date = (datetime.strptime(deadline, "%d.%m.%Y"))

#print (input_list)


today_date = datetime.today()



#calculate how many days from now till deadline
time_till = deadline_date - today_date

print (f"Dear User! - time remaining for your goal: {goal} is {time_till.days} days")
