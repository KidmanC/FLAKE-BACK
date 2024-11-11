from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:mysqlpassword@localhost:3306/firstdb"

#motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

#sesiones
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para el modelo de datos
Base = declarative_base()

# Crea una dependencia que obtenga la sesión de la base de datos
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()