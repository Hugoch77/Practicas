from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class metodos():
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return None

    def dropdown(self, value):
        Select(self.web_element).select_by_value(value)
        return None

    def click(self):
        self.web_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        self.web_element.click()
        return None

    def scrollintoview(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.web_element)
        return None

    def obtaintext(self):
        text = self.web_element.text
        return text