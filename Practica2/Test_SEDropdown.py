from selenium import webdriver
from POM_SEDropdown import SeDropdown

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
SE_Dropdown = SeDropdown(driver)

SE_Dropdown.dropdown_one().dropdown("Friday")
print(SE_Dropdown.text_one().obtaintext())
SE_Dropdown.first_selected_btn().scrollintoview()
SE_Dropdown.dropdown_two().dropdown("Ohio")
SE_Dropdown.first_selected_btn().click()
print(SE_Dropdown.text_two().obtaintext())

assert SE_Dropdown.text_two().obtaintext() == "First selected option is : Ohio", "La primera opcion seleccionada no es Ohio"
print("Test Passed")

driver.close()