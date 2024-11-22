from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Institucion(Base):
    __tablename__ = 'INSTITUCION'

    institucion_id = Column(Integer, primary_key=True)
    #numero = Column(String(10))
    localidad = Column(String(50))
    codigo_dane = Column(String(20))
    nombre = Column(String(100))
    rector = Column(String(100))
    direccion = Column(String(150))
    barrio = Column(String(50))

    #back_populates
    #aulas = relationship('Aula', back_populates='institucion', lazy="joined", uselist=True, join_depth=1)