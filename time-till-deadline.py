import datetime

user_input = raw_input("Enter your goal with a deadline separated by Colon \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
print(type(deadline))
print(datetime.datetime.strptime(deadline, "%d-%m-%Y"))
print(type(datetime.datetime.strptime(deadline, "%d-%m-%Y")))
deadline_date=datetime.datetime.strptime(deadline, "%d-%m-%Y")
print(datetime.datetime.today())
today_date = datetime.datetime.today()
#   Calculate how many days from now till deadline
remaining_days = deadline_date - today_date
print(deadline_date - today_date)
#

print("Dear User! Time Remaining for your goal  are :",remaining_days.days)
print(input_list)
