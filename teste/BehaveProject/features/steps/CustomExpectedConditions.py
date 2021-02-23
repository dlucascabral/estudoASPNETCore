class url_to_be(object):

    def __init__(self,url):
        self.url =  url

    def __call__(self, driver):
        current_url = driver.current_url
        if(current_url == self.url):
            return True
        else:
            return False

class textfield_text_to_be(object):
    
    def __init__(self, locator,text):
        self.locator = locator
        self.text = text
    
    def __call__(self,driver):
        element = driver.find_element(*self.locator)
        if(self.text == element.get_attribute("value")):
            return True
        else:
            return False

# aguarda até que o texto esperado esteja completamento inserido no input dentro do ngselect
# e que o dropdown do ngselect ja tenha sido fechado, que acontece apos o ENTER
# serve para prevenir erros de execução causados por um valor incompleto no select ou quando
# o dropdown sobrepoe algum outro elemento, tal como click intercepted

class select_text_to_be(object):

    def __init__(self, locator,text):
        self.locator = locator
        self.text = text

    def __call__(self,driver):
        element = driver.find_element(*self.locator)
        if(self.text in element.get_attribute('innerText')):
            return True
        else:
            return False

# aguarda até que o select em questão tenha pelo menos um filho do tipo ng-option
# o que deve implicar que a request que carrega as opções do select foi concluida
# evitando casos em que o texto era digitado no select, mas por causa das opções
# ainda não terem sido carregadas, o select acaba ficando vazio

class select_have_options_loaded(object):
    
    def __init__(self,locator):
        self.locator = locator
    
    def __call__(self, driver):
        print("entrou no wait")
        element = driver.find_element(*self.locator)
        try:
            element.find_element_by_class_name("ng-option")
            return True
        except:
            print("falhou no wait")
            return False
