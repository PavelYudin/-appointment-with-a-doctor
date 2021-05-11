from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def make_an_appointment(driver):
	appointment=WebDriverWait(driver,10)\
    	.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"ЗАПИСАТЬСЯ НА ПРИЕМ")))
	appointment.location_once_scrolled_into_view
	appointment.click()