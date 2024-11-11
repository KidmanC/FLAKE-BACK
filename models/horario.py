from config.database import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, Time
from schemas.dia_semana import Dia_semana


class Horario(Base):
    __tablename__ = 'HORARIO'

    horario_id = Column(Integer, primary_key=True)
    clase_id = Column(Integer, ForeignKey('CLASE.clase_id'))
    dia_semana = Column(Enum(Dia_semana))
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
