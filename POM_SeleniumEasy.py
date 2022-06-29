from selenium.webdriver.common.alert import Alert
from Base import base
from selenium.webdriver.common.by import By
from Metodos import metodos
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class selenium_easy(base):

    url = "https://demo.seleniumeasy.com/basic-first-form-demo.html"

    def popup(self):
        locator = (By.XPATH, '//a[@class="at-cv-button at-cv-lightbox-yesno at-cm-no-button"]')
        return metodos(driver=self.driver, by=locator[0], valor=locator[1])

    def first_input(self):
        locator = (By.XPATH, "//input[contains(@id,'user-message')]")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def show_message_btn(self):
        locator = (By.XPATH, "//button[@type='button'][contains(.,'Show Message')]")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def message_one(self):
        locator = (By.XPATH, "//span[@id='display']")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def input_a(self):
        locator = (By.XPATH, "//input[contains(@id,'sum1')]")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def input_b(self):
        locator = (By.XPATH, "//input[contains(@id,'sum2')]")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def get_total_btn(self):
        locator = (By.XPATH, "//button[@type='button'][contains(.,'Get Total')]")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def result(self):
        locator = (By.XPATH, "//span[contains(@id,'displayvalue')]")
        return metodos(driver=self.driver,by=locator[0], valor=locator[1])

    def alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return Alert(self.driver).accept()