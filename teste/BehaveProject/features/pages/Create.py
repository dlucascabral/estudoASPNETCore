from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


class Create(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url = self.url + "/Create"

    locators = {
        "input_nome" : (By.ID, "Book_Name"),
        "input_autor" : (By.ID, "Book_Author"),
        "input_isbn" : (By.ID, "Book_ISBN"),
        "button_create" : (By. XPATH, '//input[@value="Create"]'),
        "msg_nome_requerido" : (By.ID, 'Book_Name-error'),
    }

    def inserir_nome(self, nome):
        if (nome != 'vazio'):
            self.input_nome.send_keys(nome)

    def inserir_autor(self, autor):
        if(autor != 'vazio'):
            self.input_autor.send_keys(autor)
    
    def inserir_isbn(self, isbn):
        if(isbn != 'vazio'):
            self.input_isbn.send_keys(isbn)

    
    def clicar_botao_create(self):
        self.click("button_create")
    
    def checar_msg_nome_requerido(self):
        assert self.msg_nome_requerido.text == "The Name field is required."
    