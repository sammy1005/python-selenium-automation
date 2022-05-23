from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Chrome(executable_path='C:\\Users\\skige\\python-selenium-automation\\chromedriver.exe')
driver= webdriver.Edge(executable_path="C:\\Users\\skige\\python-selenium-automation\\msedgedriver.exe")
driver.get('https://www.amazon.com/gp/help/customer/display.html/')
search = driver.find_element(By.ID, "helpsearch")
search.clear()
search.send_keys('cancel order', Keys.ENTER)
