from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\skige\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.heartlandamerica.com/')

search=driver.find_element(By,CSS_SELECTOR,"ul li.c-form-list__item.c-form-list__item--full.c-control-group.u-flex input[placeholder='Keyword or item #']")


search.send_keys("inversion table")
search.send_keys(Keys.ENTER)
