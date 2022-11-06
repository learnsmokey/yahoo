from pages.main_page import MainPage
from pages.main_page import DirectPage


class Application:

    def __init__(self, driver):
        print("Application init started")
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.main_page = DirectPage
        print("Application init stopped")
