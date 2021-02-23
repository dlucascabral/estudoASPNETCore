from features.pages.BasePage import BasePage
from features.steps.CustomExpectedConditions import url_to_be
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from features.steps.CustomExpectedConditions import * 
from selenium.webdriver.support.wait import WebDriverWait

class Booklist (BasePage):
    def __ini__(self, context):
        BasePage.__init__(self, context)
        self.url = self.url

    def pagina_carregada(self):
        WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"]).until(
            url_to_be(self.url)
        )

        