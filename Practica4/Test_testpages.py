from selenium import webdriver
from POM_testpages import POM_testpages
import time

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
pagina = POM_testpages(driver)

pagina.first_name().send_text("Hugo")
pagina.last_name().send_text("ChavezGarcia")
pagina.age().send_text("25")
pagina.country().select("Mexico")
pagina.notes().send_text("Pagina de prueba")
pagina.send().click()

assert pagina.validation().get_text() == "Input Validation Response", "Respuesta de validacion incorrecta"
time.sleep(5)

driver.close()