# User Management with FastAPI and MySQL

This is a sample project for a user management system using FastAPI as the backend framework and MySQL as the relational database. The project allows creating, listing, and managing users.

---

# Features

- User creation with data validation.
- Listing all registered users.
- Integration with a MySQL database for persistence.

---

# Technologies Used

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PyMySQL**
- **MySQL**

---


---

# Prerequisites

- **Python 3.10+** installed.
- **MySQL** installed and configured.
- A virtual environment set up for the project.

---

# Database Setup

1. Make sure MySQL is running.

2. Create a database:
   CREATE DATABASE gerenciador_usuarios;
      CREATE DATABASE user_manager; (english version)

3. Configure the database credentials in the app/database.py file:
   SQLALCHEMY_DATABASE_URL = "mysql+pymysql://usuario:senha@localhost/gerenciador_usuarios"
      SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/user_manager" (english version)

---

# Installation and Running

1. Clone the repository:
git clone https://github.com/your-username/your-project.git
cd your-project

2. Create and activate the virtual environment:
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Start the server:
uvicorn app.main:app --reload

---
