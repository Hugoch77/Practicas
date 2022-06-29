from selenium.webdriver.common.by import By
from Base import Base
from Practica3.Metodos import Metodos


class POM_iframe(Base):

    url = "https://demoqa.com/frames"

    def text_one(self):
        locator = (By.XPATH, "(//div[contains(.,'Sample Iframe page There are 2 Iframes in this page. Use browser inspecter or firebug to check out the HTML source. In total you can switch between the parent frame, which is this window, and the two frames below')])[7]")
        return Metodos(driver=self.driver, by=locator[0], value=locator[1])

    def iframe(self):
        locator = (By.ID, "frame1")
        return Metodos(driver=self.driver, by=locator[0], value=locator[1])

    def text_two(self):
        locator = (By.XPATH, "//h1[contains(@id,'sampleHeading')]")
        return Metodos(driver=self.driver, by=locator[0], value=locator[1])

    def scroll(self):
        locator = (By.XPATH, "(//div[contains(@class,'header-text')])[5]")
        return Metodos(driver=self.driver, by=locator[0], value=locator[1])