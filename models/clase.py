from config.database import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey
from schemas.grado import Grado


class Clase(Base):
    __tablename__ = 'CLASE'

    clase_id = Column(Integer, primary_key=True)
    aula_id = Column(Integer, ForeignKey('AULA.aula_id'))
    tutor_id = Column(Integer, ForeignKey('TUTOR.tutor_id'))
    periodo_id = Column(Integer, ForeignKey('PERIODO.periodo_id'))
    grado = Column(Enum(Grado))