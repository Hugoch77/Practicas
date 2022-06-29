from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("")
driver.maximize_window()
