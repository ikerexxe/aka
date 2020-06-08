import time
import sys

from user import User
from web_management import *
from file_management import *

# Debug variables
debug = True
headless = False

def parse_args(argv):
	# Loading debug information
	if(argv[0] == "1"):
		debug = True
		headless = False
	elif(argv[0] == "0"):
		debug = False
		headless = True
	else:
		print("Incorrect first argument")
		sys.exit(1)

def main(argv):
	parse_args(argv)
	user = load_file()

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
	main(sys.argv[1:])
