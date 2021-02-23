from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, context):
        self.context = context
        self.url = context.variables["url"]
        self.locator = {}

    def find_element(self, *loc):
        return self.context.browser.find_element(*loc)
    
    def navigate_to(self):
        self.context.browser.get(self.url)

    def click(self, element_locator):
        # Aguarda o item ser clicável antes de clicar
        WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"]).until(
            expected_conditions.element_to_be_clickable(self.locators[element_locator])
        )

        # o execute_script com lcick por comando javascript se mostoru mais estável que o click() do selenium
        self.context.browser.execute_script('arguments[0].click();' , self.find_element(*self.locators[element_locator]))

    def select(self, element_locator, text):
        # Aguarda o elemento
        WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"]).until(
            expected_conditions.element_to_be_clickable(self.locators[element_locator])
        )

        # Aguarda as opções do select serem carregadas
        # Assumindo que ocorreu a exibição de um, implica que todos as opções foram carregadas
        # por serem originadas da mesma request
    
        ngselect = self.find_element(*self.locators[element_locator])
        input = ngselect.find_element_by_tag_name('input')
        input.send_keys(text)

        input.send_keys(Keys.ENTER)
        
        WebDriverWait(self.context.browser, self.context.variables["element_load_timeout"]).until(
            expected_conditions.visibility_of_element_located(self.locators[item])
        )
    
    def __getattr__(self, item):
        if item in self.locators.keys():
            WebDriverWait (self.context.browser, self.context.variables["element_load_timeout"]).until(
                expected_conditions.visibility_of_element_located(self.locators[item])
            )

            return self.find_element(*self.locators[item])
        else:
            raise AttributeError("'Basepage' object has no attribute" + item )
        