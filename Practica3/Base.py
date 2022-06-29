class Base(object):

    url = None

    def __init__(self, driver):
        self.driver = driver
        self.go()

    def go(self):
        self.driver.get(self.url)
        self.driver.maximize_window()