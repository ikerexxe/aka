from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def user_authentication(headless, iker):
	DRIVER_PATH = "./chromedriver"
	WEB_PAGE = "https://www.donostia.eus/donostiakirola/kirolekintzak/login.aspx?idioma=ES"

	if(headless):
		options = Options()
		options.set_headless()
		assert options.headless # Operating in headless mode
		driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
	else:
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

def installation(driver):
	box = driver.find_element_by_id("MainContent_MainContent_cboFiliales")
	for option in box.find_elements_by_tag_name('option'):
		if option.text in "PACO YOLDI":
			option.click()
	try:
		link = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "MainContent_MainContent_gridReservas"))
		)
		link.click()

		return driver
	except:
		driver.quit()

def select_date(driver):
	xpath = "//*[@class='day dialibre' and @data-day='08/06/2020']"
	try:
		link = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, xpath))
		)
		link.click()

		return driver
	except:
		driver.quit()

def select_hour(driver):
	xpath = "//tr[10]/td[1]"
	try:
		link = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, xpath))
		)
		print(link.text)
		link.click()

		return driver
	except:
		driver.quit()
