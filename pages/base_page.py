from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        print("Base Page init started")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        print("Base Page init stopped")

    def open_page(self, url):
        print("Base open page started")
        self.driver.get(url)
        print("Base open page stopped")
