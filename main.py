import time

from user import User
from web_management import *

headless = False

def main():
	iker = User()
	main_driver = user_authentication(headless, iker)
	driver = reservation(main_driver)
	driver = installation(driver)
	driver = select_date(driver)
	driver = select_hour(driver)

	time.sleep(5)
	main_driver.close()

if __name__ == "__main__":
	main()
