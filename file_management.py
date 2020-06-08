from user import User

def load_file():
	file_object = open("aka.conf", "r")

	# First line is just a comment to identify the user
	file_object.readline()
	
	dni = file_object.readline().rstrip()
	cont = file_object.readline().rstrip()
	inst = file_object.readline().rstrip()
	date = file_object.readline().rstrip()
	hour = file_object.readline().rstrip()

	file_object.close()

	user = User(dni, cont, inst, date, hour)

	return user
