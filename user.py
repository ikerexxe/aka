class User:

	def __init__(self):
		file_object = open("aka.conf", "r")

		# First line is just a comment to identify the user
		file_object.readline()
		
		self.dni = file_object.readline().rstrip()
		self.cont = file_object.readline().rstrip()

		file_object.close()
