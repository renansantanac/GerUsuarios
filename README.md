# Gerenciamento de Usuários com FastAPI e MySQL

Este é um projeto de exemplo para um sistema de gerenciamento de usuários utilizando **FastAPI** como framework backend e **MySQL** como banco de dados relacional. O projeto permite criar, listar e gerenciar usuários.

---

# Funcionalidades

- Criação de usuários com validação de dados.
- Listagem de todos os usuários cadastrados.
- Integração com um banco de dados MySQL para persistência.

---

# Tecnologias utilizadas

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PyMySQL**
- **MySQL**

---


---

# Pré-requisitos

- **Python 3.10+** instalado.
- **MySQL** instalado e configurado.
- Um ambiente virtual configurado para o projeto.

---

# Configuração do Banco de Dados

1. Certifique-se de que o MySQL está em execução.
2. Crie um banco de dados:
   ```sql
   CREATE DATABASE gerenciador_usuarios;
3. Configure as credenciais do banco no arquivo app/database.py:
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://usuario:senha@localhost/gerenciador_usuarios"

---

# Instalação e Execução

1. Clone o repositório
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto

2. Crie e ative o ambiente virtual:
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Inicie o servidor:
uvicorn app.main:app --reload

---