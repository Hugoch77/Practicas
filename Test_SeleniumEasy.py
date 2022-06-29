from selenium import webdriver
from POM_SeleniumEasy import selenium_easy

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

testseleniumeasy = selenium_easy(driver=driver)

testseleniumeasy.popup().click_btn()
testseleniumeasy.first_input().send_text("Hugo")
testseleniumeasy.show_message_btn().click_btn()
print(testseleniumeasy.message_one().obtaintext())
testseleniumeasy.input_a().send_text("13")
testseleniumeasy.input_b().send_text("2")
testseleniumeasy.get_total_btn().click_btn()
print(testseleniumeasy.result().obtaintext())

driver.close()