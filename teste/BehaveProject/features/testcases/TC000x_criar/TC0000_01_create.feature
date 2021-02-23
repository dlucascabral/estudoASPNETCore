#language: pt
@sprint9 @create @all
@TC0000_xx

Funcionalidade: Create livro em CRUD BookListRazor

#CasodeSucesso
@createsucesso
Esquema do Cenário: Create Efetuado com Sucesso
    Dado que esteja na página create
    Quando insiro <nome> no campo name do create
    E insiro <autor> no campo author do create
    E insiro <isbn> no campo isbn do create
    E clico no botão create do create
    Então verifico que a booklist foi carregada

    Exemplos:
        | nome        | autor    | isbn        |
        | TesteAoVivo | Eu Mesmo | 11211215815 |

#CasodeInsucesso

@createfalha
Esquema do Cenário: Create Sem sucesso
    Dado que esteja na página create
    Quando insiro <nome> no campo name do create
    E insiro <autor> no campo author do create
    E insiro <isbn> no campo isbn do create
    E clico no botão create do create
    Então verifico que obtive o resultado <resultadoEsp>

    Exemplos: 
        | nome       | autor   | isbn       | resultadoEsp               |
        | empty      | dev@123 | 5135115313 | The Name field is required.|