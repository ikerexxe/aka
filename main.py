import time

from user import User
from web_management import *

# Debug variables
debug = True
headless = False

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

def main():
	user = load_file()

	# Loading debug information
	if(debug):
		headless = False

	main_driver = user_authentication(headless, user)
	driver = reservation(main_driver)
	driver = installation(driver, user.inst)
	driver = select_date(driver, user.date)
	driver = select_hour(driver, user.hour)
	if(not debug):
		driver = reserve(driver)

	time.sleep(5)
	main_driver.quit()

if __name__ == "__main__":
	main()
