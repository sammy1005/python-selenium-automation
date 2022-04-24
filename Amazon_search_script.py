from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path='C:\\Users\\skige\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Edge(executable_path="C:\\Users\\skige\\python-selenium-automation\\msedgedriver.exe")
driver.get('https://www.bing.com/')

driver.find_element(By.ID, 'sb_form_q').send_keys('typing test')

driver.find_element(By.ID, 'search_icon').click()