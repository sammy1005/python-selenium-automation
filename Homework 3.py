from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path='C:\\Users\\skige\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Edge(executable_path="C:\\Users\\skige\\python-selenium-automation\\msedgedriver.exe")
driver.get('https://www.stubhub.com/')
driver.find_element(By.CSS_SELECTOR, 'span.mh__nav-menu-icon.menu__icon-sign-in').click()
driver.find_element(By.CSS_SELECTOR, 'a.auth-link.signup').click()
