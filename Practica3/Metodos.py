from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Metodos():
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find()

    def find(self):
        self.web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        return None

    def goiframe(self):
        iframe = self.web_element
        self.driver.switch_to.frame(iframe)
        return None

    def gettext(self):
        text = self.web_element.text
        return text

    def scroll(self):
        action = ActionChains(self.driver)
        action.scroll_to_element(self.web_element)
        return None