import time

from user import User
from web_management import *

def main():
	iker = User()
	main_driver = user_authentication(iker)
	driver = reservation(main_driver)
	driver = installation(driver)

	time.sleep(5)
	main_driver.close()

if __name__ == "__main__":
	main()
