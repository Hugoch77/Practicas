from selenium import webdriver
from POM_iframe import POM_iframe
from Metodos import Metodos
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

Test_iframe = POM_iframe(driver)

print(Test_iframe.text_one().gettext())
Test_iframe.iframe().goiframe()
print(Test_iframe.text_two().gettext())
driver.switch_to.default_content()
print(Test_iframe.text_one().gettext())
Test_iframe.scroll().scroll()
print("Scroll completado")
driver.close()