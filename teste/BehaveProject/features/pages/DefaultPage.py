from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By 
import time 

class DefaultPage (BasePage):
    def __init__(self,context):
        BasePage.__init__(self, context)
        self.url = self.url + "#"

    locators = {
        
    }