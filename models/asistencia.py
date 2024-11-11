from config.database import Base
from sqlalchemy import Column, Date, Enum, Integer, ForeignKey
from schemas.presente import Presente


class Asistencia(Base):
    __tablename__ = 'ASISTENCIA'

    asistencia_id = Column(Integer, primary_key=True)
    clase_id = Column(Integer, ForeignKey('CLASE.clase_id'))
    estudiante_id = Column(Integer, ForeignKey('ESTUDIANTE.estudiante_id'))
    fecha = Column(Date)
    presente = Column(Enum(Presente, values_callable=lambda enum: [e.value for e in enum]))