# Controle de vendas

Descrição para executar o projeto e utilizar a sua API


### Instalação


Na mesma pasta do arquivo docker-compose execute (Caso o docker já instalado):
```
sudo docker-compose up --build
```
Esse comando vai criar os container e imagens docker e executar o projeto, que por sua vez poderá ser acessado na url local [http://localhost:8000/](http://localhost/:8000)


### Requisitos da plataforma:

* Só pode ser acessível pelos vendedores a partir de um login e senha
    * Para ter acesso aos endpoints é necessário autenticação por token e o usuario autenticado tem que estar no grupo de vendedores, já criado no banco.
    * Para obter o token é necessario enviar uma requisição post para o endpoint http://localhost:8000/api-token-auth/ com username e password no body. Exemplo:
    ```
    {
        "username": "vendedor1",
        "password": "senhaven1"
    } 
    ```
    * O projeto em questão é executado com um banco de dados sqlite3 já com alguns dados cadastrados e o usuário vendedor1 (senha: senhaven1) para testes. 
* Deve listar os pedidos e os produtos
    * Para listar os produtos enviar requisição com o método GET para o endpoint http://localhost:8000/produtos/. Não esquecer do token no cabeçalho para autenticação e permissão.
    * Para listar os pedidos enviar requisição com o método GET para o endpoint http://localhost:8000/pedidos/. Não esquecer do token no cabeçalho para autenticação e permissão.
* Necessário poder ver e editar os detalhes dos pedidos e dos produtos:
    * Para vê detalhes de um pedido enviar requisição GET para http://localhost:8000/pedidos/pk/. A palavra chave "pk" deve ser substituida pelo ID do produto desejado.
    
        Para alterar um campo deve-se enviar uma requisição do tipo PATCH para http://localhost:8000/pedidos/pk/. No body deve conter o novo valor do campo, exemplo:
            
            ```
            {
            "numeroPedido": "333"
            } 
            ```
        O valor do campo "numeroPedido" será alterado para "333".
    * Para detalhes dos produtos é só seguir os mesmos passos realizado para pedidos. Endpoint http://localhost:8000/produtos/pk/
* Possibilidade de gerar um relatório detalhado de pedidos, que possa ser ordenado por valor, ou data de compra. O relatório precisa ser paginado.
    * O tipo de paginação utilizada foi a de Offset e Limit. No offset especifica a partir de qual registro você quer os dados, e no limit você especifica o limite de registros a serem retornados.
    * Além dos parametros "offset" e "limit", também tem a opção do parametro "orderby". Se no orderby for passado o nome "valor" o relatório vem ordenado pelo valor do pedido, se for passado "data" os pedidos vem em ordenados pela data da compra. 
    * Exemplo de endpoint com filtros para o relatório: http://localhost:8000/relatorio/?limit=3&offset=3&orderby=valor . Esse endpoint vai retortar 3 registros, iniciando do terceiro, ordenados pelo valor do pedido.
    
    
OBS:. O banco de dados já tem um usuário que pode ser utilizado para teste, caso desejado. As credenciais são
        username: admin e
        password: senhaadmin1 superusuario com todos os poderes e username: vendedor1 | password: senhaven1
        



## Executado com

* [Sqlite3] - Versão Docker 
* [Python 3.8] linguagem
* [Django 3.2.5](https://www.djangoproject.com/) - Framework usado em conjunto com o Django Rest Framework para criação de API's REST
* [Docker] - Usado para testes locais

## Autores

* **Deocleci dos Santos Dias** - *Desenvolvedor* 


