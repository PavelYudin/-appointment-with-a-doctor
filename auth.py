def auth(driver,number_police,dob):
    form = driver.find_element_by_css_selector("form[name='registry-form']")
    number_oms = form.find_element_by_name('nPol')
    date = form.find_element_by_name('birthday')
    submit = form.find_element_by_css_selector("a[href='#']")
    number_oms.send_keys(number_police)#5050800841001408
    date.send_keys(dob)
    submit.click()