from behave import *
from features.pages.Create import Create
from features.pages.Booklist import Booklist

@step("que esteja na página create")
def step_impl(context):
    Create(context).navigate_to()

@step("insiro {nome} no campo name do create")
def step_impl(context, nome):
    if(nome != "empty"):
        Create(context).inserir_nome(nome)
    else:
        Create(context).inserir_nome("")

@step("insiro {autor} no campo author do create")
def step_impl(context, autor):
    Create(context).inserir_autor(autor)

@step("insiro {isbn} no campo isbn do create")
def step_impl(context, isbn):
    Create(context).inserir_isbn(isbn)

@step("clico no botão create do create")    
def step_impl(context):
    Create(context).clicar_botao_create()

@step("verifico que a booklist foi carregada")
def step_impl(context):
    Booklist(context).pagina_carregada()

@step("verifico que obtive o resultado {resultadoEsp}")
def step_impl(context, resultadoEsp):
    if(resultadoEsp == "The Name field is required."):
        Create(context).checar_msg_nome_requerido()
    

