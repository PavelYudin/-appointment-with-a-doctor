from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def find_time(driver,interval_time):
    block_time = WebDriverWait(driver, 30) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR,".b-app-time" )))
    block_appointment_time = block_time.find_elements_by_css_selector("[onclick]")
    appointment_time='Свободных талонов в заданный временной промежуток не обнаружено'
    if(interval_time):
        for i in block_appointment_time:
            hour=int(i.text.split(":")[0])
            if(hour>=int(interval_time[0]) and hour<=int(interval_time[1])):
                appointment_time=i
                break
    else:
        appointment_time=block_appointment_time[0]
    return appointment_time