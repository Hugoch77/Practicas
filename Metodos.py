from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

class metodos():
    def __init__(self, driver, by, valor):
        self.driver = driver
        self.by = by
        self.valor = valor
        self.locator = (self.by, self.valor)
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        self.web_element = element
        return None

    def send_text(self, text):
        self.web_element.send_keys(text)
        return None

    def click_btn(self):
        self.element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        self.element.click()
        return None

    def dropdown(self, index):
        Select(self.web_element).select_by_index(index)
        return None

    def scrollto(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.web_element)
        return None

    def obtaintext(self):
        text = self.web_element.text
        return text