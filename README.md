# Sistema de Doações Usuário → Usuário

Um sistema web desenvolvido em **Flask** para permitir que usuários façam doações para outros usuários.  
O projeto inclui **CRUD de doações**,**Automacao de testes basica com Selenium**, autenticação de usuários e interface interativa com **HTML, CSS e JavaScript**.

---

##  Tecnologias utilizadas

- **Python 3.13**
- **Selenium** – para testes automaticos
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
- ├── relatorios/ #onde aparecem os arquivos .txt das movimentacoes e dos produtos
- ├── erros/ # onde ira aramzenar as imagens da tela quando houver erros
- │ │   └──erro_{timestamp}.png
- ├── testes/ # Script do teste automatico em selenium
- │ │   └──teste.py
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
- testes automaticos basicos,com geracao de relatorio em .txt de resultados e registro de imagem de erros em .png
- criptografia de senha basica com werkzeug.security
- Visualizar doações de outros usuários
- Formulários interativos que podem ser mostrados ou ocultados
- Interface simples e intuitiva
- Controle de movimentacoes

---
## Observacoes
- O projeto precisa de python 3.13 ou acima e ter o framework flask,selenium,webdriver.chrome e sqlalchemy instalados.
- Antes de rodar a aplicacao execute o arquivo.sql em seu workbench para criar o banco e crie a conexao ,alem de alterar a variavel sua senha do banco pra sua senha real do banco.
- No arquivo,testes.py,o id usado pode nao existir em seu banco,pra que o teste funcione,voce deve criar um cadastro no banco e alterar a variavel produto_id pro respectivo id desse elemento(o estoque dele deve ser maior que 0 pra que a aplicacao funcione).
- Tambem no testes.py,voce precisa ter um cadastro com email jose@gmail.com e senha 123 no seu banco de dados,ou outro email e senha de usuario cadastrado nesses campos para a automação funcionar da forma desejada.
---
## Instalacao de frameworks:
- os comandos a seguir instalam as bibliotecas necessarias para rodar a aplicação:

```bash
# clonar repositório
git clone https://github.com/ldm-code/doacoes.git
cd doacoes

# apos isso configrar ambiente

# Para linux/macOS use:
python3 -m venv .venv
source .venv/bin/activate

# Para Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalando as dependencias do projeto:
pip install Flask
pip install SQLAlchemy
pip install selenium
```
