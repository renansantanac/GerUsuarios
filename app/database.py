from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão para o MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://usuario:senha@localhost/nome_do_banco"

# Criando o engine para conexão com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})

# Configurando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos do SQLAlchemy
Base = declarative_base()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)
