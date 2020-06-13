from user import User

''' Configuration file format:
Comment to identify the user
DNI
Password
Installation
Day of the week
Time
* The previous two lines can be repeated as many times as needed
Blank line
* Start again from top for another user
'''

def load_file():
	users = []

	file_object = open("aka.conf", "r")

	# First line is just a comment to identify the user
	next_user = file_object.readline()

	while(next_user.strip()):
		dates = []
		hours = []

		dni = file_object.readline().rstrip()
		cont = file_object.readline().rstrip()
		inst = file_object.readline().rstrip()
		date = file_object.readline().rstrip()

		while date:
			dates.append(date)
			hour = file_object.readline().rstrip()
			hours.append(hour)
			date = file_object.readline().rstrip()

		users.append(User(dni, cont, inst, dates, hours))
		next_user = file_object.readline()

	file_object.close()

	return users
