from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def check_exist_doctor(driver,surname_doctor):
	try:
		doctor = WebDriverWait(driver, 10) \
			.until(EC.presence_of_element_located((By.XPATH,'.//h4[contains(text(),"{0}")]'.format(surname_doctor))))
		return doctor
	except TimeoutException:
		print("Данного врача не существует!")
		return None