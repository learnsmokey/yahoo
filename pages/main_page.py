from pages.base_page import BasePage


class MainPage(BasePage):

    def open_webpage(self, MyURL):
        print("Main Open_webpage call started")
        self.open_page(url=MyURL)
        print("Main Open_webpage call stopped")


class DirectPage:

    # def __init__(self, driver):
    #     self.driver = driver

    def open_direct_webpage(self, MyURL):
        print("Direct Open call started")
        self.driver.get(url=MyURL)
        print("Direct Open call stopped")
