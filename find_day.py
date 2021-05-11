from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from check_exist_doctor import check_exist_doctor
def find_day(driver,str_js,unwanted_date,surname_doctor):
        doctor = check_exist_doctor(driver, surname_doctor)
        if (doctor is None):
            print("no doctor")
            return True
        parent_elem = WebDriverWait(doctor, 10) \
            .until(EC.presence_of_element_located((By.XPATH,"../..")))
        driver.execute_script("arguments[0].id='required_element'",parent_elem)#устанавливаем для блока с днями аттр id для удобного поиска
        reception_day=driver.execute_script(str_js,unwanted_date)
        return reception_day
