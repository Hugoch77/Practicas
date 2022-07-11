from selenium.webdriver.common.by import By
from Base import base
from Metodos import metodos


class POM_testpages(base):

    url = "https://testpages.herokuapp.com/styled/validation/input-validation.html"

    def first_name(self):
        locator = (By.XPATH, "//input[contains(@id,'firstname')]")
        return metodos(self.driver, by=locator[0], value=locator[1])

    def last_name(self):
        locator = (By.XPATH, "//input[@id='surname']")
        return metodos(self.driver, by=locator[0], value=locator[1])

    def age(self):
        locator = (By.XPATH, "//input[@id='age']")
        return metodos(self.driver, by=locator[0], value=locator[1])

    def country(self):
        locator = (By.XPATH, "//select[@id='country']")
        return metodos(self.driver, by=locator[0], value=locator[1])

    def notes(self):
        locator = (By.XPATH, "//textarea[@id='notes']")
        return metodos(self.driver, by=locator[0], value=locator[1])

    def send(self):
        locator = (By.XPATH, "//input[@type='submit']")
        return metodos(self.driver, by=locator[0], value=locator[1])

    def validation(self):
        locator = (By.XPATH, "//h1[contains(.,'Input Validation Response')]")
        return metodos(self.driver, by=locator[0], value=locator[1])