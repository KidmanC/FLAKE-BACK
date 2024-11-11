from config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric


class Nota(Base):
    __tablename__ = 'NOTA'

    nota_id = Column(Integer, primary_key=True)
    periodo_id = Column(Integer, ForeignKey('PERIODOLECTIVO.periodo_id'))
    estudiante_id = Column(Integer, ForeignKey('ESTUDIANTE.estudiante_id'))
    clase_id = Column(Integer, ForeignKey('CLASE.clase_id'))
    bloque = Column(Integer) 
    calificacion = Column(Numeric)