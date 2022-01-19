## Flask_Apps
### Desenvolvendo aplicativos básicos para entender os conceitos de uma aplicação utilizando o Flask
#### Aplicativos desenvolvidos

<ul>
    <b>Hello_World</b>
    <li>Objetivo: Entender o básico do básico</li>
    <li>Funcionamento: Apenas uma tela de Hello World</li> 
</ul>
<ul>
    <b>DB_Simples</b>
    <li>Objetivo: Entender como usar db no flask</li>
    <li>Funcionamento: Cria um database com duas tabelas "Users" e "Pokemons". É possivel criar usuários e atribuir pokemons a esses usuários</li> 
</ul>
<ul>
    <b>Autenticação_Simples</b>
    <li>Objetivo: Implementar autenticação utilizando flask-login e formulários; Implementar testes de login utilizando pytest</li>
    <li>Funcionamento: Cria um database com uma tabela "Users". É possivel se registrar, logar e quando logado apagar usuários. Também podemos utilizar o pytest para testar as funções básicas da aplicação</li>
</ul>
<ul>
    <b>Envio_Email</b>
    <li>Criado a partir do App: Autenticação_Simples</li>
    <li>Objetivo: Implementar o envio de e-mails com anexos</li>
    <li>Funcionamento: Quando um usuário é cadastrado um e-mail de boas-vindas é enviado com um arquivo txt em anexo. É necessário configurar a função manda_email do arquivo functions.py com um e-mail válido!</li>
</ul>
<ul>
    <b>API_Simples</b>
    <li>Criado a partir do App: Autenticação_Simples</li>
    <li>Objetivo: Implementar uma API simples</li>
    <li>Funcionamento: GET pega os nomes dos usuários, POST cadastra um usuário, PUT modifica a senha de um usuário, DELETE deleta um usuário</li>
</ul>

#### Rodando os apps

- Criar ambiente virtual (python -m venv .venv)
- Entrar no ambiente virtual (.venv\Scripts\activate)
- Instalar os requisitos (pip install -r requirements.txt)
- Entrar no app de interesse (cd "app de interesse")
- Rodar o app (python app.py)

