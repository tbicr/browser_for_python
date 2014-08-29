from selenium import webdriver


driver = webdriver.Firefox()
driver.set_window_size(1280, 768)
driver.get('https://www.python.org/accounts/login/')

driver.find_element_by_id('id_login').send_keys('user')
driver.find_element_by_id('id_password').send_keys('password')
driver.find_element_by_css_selector('.primaryAction').click()

feblt = driver.find_element_by_link_text
action = webdriver.ActionChains(driver)
action.move_to_element(feblt('Sign Out')).perform()
driver.implicitly_wait(0.5)

action.move_to_element(feblt('View your public profile')).perform()
action.click().perform()

driver.quit()
