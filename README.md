### Flask_Apps ###

#### Aplicativos desenvolvidos ####

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
    <li>Funcionamento: Quando um usuário é cadastrado um e-mail de boas vindas é enviado com um arquivo txt em anexo</li>
</ul>

#### Rodando os apps ####

- Criar ambiente virtual (python -m venv .venv)
- Entrar no ambiente virtual (.venv\Scripts\activate)
- Instalar os requisitos (pip install -r requirements.txt)
- Entrar no app de interesse (cd "app de interesse")
- Rodar o app (python app.py)

