from behave import *
from features.pages.Create import Create
from features.pages.DefaultPage import DefaultPage
from features.pages.Booklist import Booklist
import time

@step('que esteja logado com tipo de operador interno')
def step_impl(context):
    Login(context).navigate_to()
    Login(context).inserir_cpf(context.variables['CPF'])
    Login(context).inserir_senha(context.variables['password'])
    Login(context).selecionar_operador(context.variables['tipoOperador'])
    Login(context).clicar_botao_login()
    Dashboard(context).pagina_carregada()

@step('que tenha cadastrado Dados Principais da Obra/Servico com os seguintes dados')
def step_impl(context):
    context.execute_steps('''
        Dado que esteja na pagina de cadastro de obra e serviço
        E seleciono a unidade gestora {unidadeGestora}
        E seleciono a forma de execução {formaExecucao}
        E preencho o campo de nome do objeto {nomeObjeto}
        E seleciono o tipo de obra {tipoObra}
        E seleciono o tipo de intervenção {tipoIntervencao}
        E seleciono o Setor Beneficiario {setorBeneficiario}
        E clico no botão de salvar os dados principais
        Então verifico que o cadastro de Dados Principais foi realizado com sucesso
    '''.format(unidadeGestora=context.table[0]['unidadeGestora'], formaExecucao=context.table[0]['formaExecucao'], 
                nomeObjeto=context.table[0]['nomeObjeto'], tipoObra=context.table[0]['tipoObra'], 
                tipoIntervencao=context.table[0]['tipoIntervencao'], setorBeneficiario=context.table[0]['setorBeneficiario']))
