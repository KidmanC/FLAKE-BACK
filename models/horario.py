from config.database import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, Time
from sqlalchemy.orm import relationship
from schemas.dia_semana import Dia_semana


class Horario(Base):
    __tablename__ = 'HORARIO'

    horario_id = Column(Integer, primary_key=True)
    clase_id = Column(Integer, ForeignKey('CLASE.clase_id'))
    dia_semana = Column(Enum(Dia_semana, values_callable=lambda enum: [e.value for e in enum]))
    hora_inicio = Column(Time)
    hora_fin = Column(Time)

    clase = relationship('Clase', backref='horarios', lazy="joined")
