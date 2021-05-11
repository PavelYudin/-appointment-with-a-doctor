from selenium import webdriver
from auth import auth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from js import js
from input import input_data
import time
from mail import send_mail
from make_an_appointment import make_an_appointment
from choose_a_dentist import choose_a_dentist
from find_day import find_day
from find_time import find_time
from final_recording import final_recording
from apscheduler.schedulers.background import BlockingScheduler

number_police,dob,surname_doctor,step,unwanted_date,interval_time,mail=input_data()
str_js=js()
def run():
	driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
	driver.get('https://uslugi.mosreg.ru/zdrav/')
	driver.maximize_window()
	auth(driver,number_police,dob)
	make_an_appointment(driver)
	choose_a_dentist(driver)
	reception_day=find_day(driver,str_js,unwanted_date,surname_doctor)
	if(reception_day is None):
		#print("на первой неделе нет талонов")
		next_week = WebDriverWait(driver, 10) \
			.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".b-doc-record-header-nav__item.next.c-next-week")))
		next_week.click()
		reception_day=find_day(driver,str_js,unwanted_date,surname_doctor)
		if(reception_day is None):
			#print("на второй неделе нет талонов")
			driver.quit()
			return
	reception_day.click()
	appointment_time=find_time(driver,interval_time)
	if(type(appointment_time) is str):#если талонов нет в заданное время
		#Здесь следующая итерация
	    #print(appointment_time)
	    driver.quit()
	    return
	    #Здесь следующая итерация
	else:
	    appointment_time.click()#click time
	    print("последняя стадия")
	    final_recording(mail,driver)
	    print('Записан')
	    send_mail(mail,'Записан!')
	    exit()
run()
scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', minutes=step,id='run')
scheduler.start()