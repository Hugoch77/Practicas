from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver


class metodos(object):

    def __init__(self, driver, by, value):
        self.web_element = None
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return None

    def send_text(self, text):
        self.web_element.send_keys(text)
        return None

    def select(self, valor):
        Select(self.web_element).select_by_value(valor)
        return None

    def click(self):
        self.web_element.click()
        return None

    def get_text(self):
        text = self.web_element.text
        return text