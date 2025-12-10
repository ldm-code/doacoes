# Sistema de Doações Usuário → Usuário

Um sistema web desenvolvido em **Flask** para permitir que usuários façam doações para outros usuários.  
O projeto inclui **CRUD de doações**, autenticação de usuários e interface interativa com **HTML, CSS e JavaScript**.

---

##  Tecnologias utilizadas

- **Python 3.13**
- **Flask** – framework web
- **SQLAlchemy** – ORM para banco de dados
- **MySQL** – banco de dados 
- **HTML / CSS / JavaScript** – frontend interativo

---

## Estrutura do projeto

- doacoes/
- │
- ├── manage.py # Arquivo principal para rodar a aplicação
- ├── dados/ # Scripts .sql do banco de dados
- │ │   └──banco.sql
- ├── static/
- │ ├── css/ # Arquivos de estilo
- │ │   ├── doar.css
- │ │   ├── usuario.css
- │ │   ├── inicial.css
- │ │   └── login.css
- │ └── js/ # JavaScript
- │ │   └──inicial.js
- ├── templates/ # arquivos.html do projeto
- │ │   ├── doar.html
- │ │   ├── movimentacoes.html
- │ │   ├── usuario.html
- │ │   ├── inicial.html
- │ │   └── login.html
- └── README.md

---

##  Funcionalidades

- Cadastro e login basico de usuários
- CRUD simples
- criptografia de senha basica com werkzeug.security
- Visualizar doações de outros usuários
- Formulários interativos que podem ser mostrados ou ocultados
- Interface simples e intuitiva
- Controle de movimentacoes

---
## Observacoes
- o projeto precisa de python 3.13 ou acima e ter o framework flask e sqlalchemy instalados
- antes de rodar a aplicacao execute o arquivo.sql em seu workbench para criar o banco e crie a conexao ,alem de alterar a variavel sua senha do banco pra sua senha real do banco.
