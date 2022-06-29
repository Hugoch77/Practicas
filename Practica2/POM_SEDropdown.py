from selenium.webdriver.common.by import By
from Base import base
from Metodos import metodos


class SeDropdown(base):

    url = "https://demo.seleniumeasy.com/basic-select-dropdown-demo.html"

    def dropdown_one(self):
        locator = (By.XPATH, "//select[contains(@id,'select-demo')]")
        return metodos(driver=self.driver, by=locator[0], value=locator[1])

    def text_one(self):
        locator = (By.XPATH, "//p[contains(@class,'selected-value')]")
        return metodos(driver=self.driver, by=locator[0], value=locator[1])

    def dropdown_two(self):
        locator = (By.XPATH, "//select[contains(@id,'multi-select')]")
        return metodos(driver=self.driver, by=locator[0], value=locator[1])

    def first_selected_btn(self):
        locator = (By.XPATH, "//button[contains(@id,'printMe')]")
        return metodos(driver=self.driver, by=locator[0], value=locator[1])

    def text_two(self):
        locator = (By.XPATH, "//p[contains(@class,'getall-selected')]")
        return metodos(driver=self.driver, by=locator[0], value=locator[1])