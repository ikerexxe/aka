import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from user import User

def user_authentication(iker):
	DRIVER_PATH = "./chromedriver"
	WEB_PAGE = "https://www.donostia.eus/donostiakirola/kirolekintzak/login.aspx?idioma=ES"

	driver = webdriver.Chrome(DRIVER_PATH)
	driver.get(WEB_PAGE)

	web_dni = driver.find_element_by_id("MainContent_MainContent_a2txtCodigo_txtA2TextBox")
	web_dni.send_keys(iker.dni)
	web_cont = driver.find_element_by_id("MainContent_MainContent_a2txtPassword_txtA2TextBox")
	web_cont.send_keys(iker.cont)
	web_cont.send_keys(Keys.RETURN)

	return driver

def reservation(driver):
	try:
		link = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.LINK_TEXT, "Reserva previa"))
		)
		link.click()
		link = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "MainContent_cmdCitaPrevia"))
		)
		link.click()

		return driver
	except:
		driver.quit()

def instalation(driver):
	box = driver.find_element_by_id("MainContent_MainContent_cboFiliales")
	for option in box.find_elements_by_tag_name('option'):
		if option.text in "PACO YOLDI":
			option.click()

def main():
	iker = User("test1", "test2")
	main_driver = user_authentication(iker)
	driver = reservation(main_driver)
	driver = instalation(driver)

	time.sleep(5)
	main_driver.close()

if __name__ == "__main__":
	main()
