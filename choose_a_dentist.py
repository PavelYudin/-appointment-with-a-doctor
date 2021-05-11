from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def choose_a_dentist(driver):
	appointment=WebDriverWait(driver, 10)\
	    .until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Стоматология терапевтическая")))
	appointment.click()
