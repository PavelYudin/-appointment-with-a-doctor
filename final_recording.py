from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def final_recording(mail,driver):
    if(mail):
        input_email = WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.ID, "to_make_an_appointment_email")))
        input_email.send_keys(mail)
        print("есть мэйл")
    else:
        checkbox = WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.ID, "to_make_an_appointment_email_confirm_agree")))
        driver.execute_script("arguments[0].checked=false", checkbox)
    final_appointment = WebDriverWait(driver, 10) \
    	.until(EC.presence_of_element_located((By.CSS_SELECTOR,".b-btn.c-step")))
    print(final_appointment.text,'999999999999999999999999999')
    final_appointment.click()
    #time.sleep(50)