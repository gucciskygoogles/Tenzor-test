from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_clickable(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout)\
                .until(EC.presence_of_element_located((how, what))).click()
        except TimeoutException:
            return False
        return True