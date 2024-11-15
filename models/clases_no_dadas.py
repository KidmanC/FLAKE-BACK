from config.database import Base
from sqlalchemy import Column, Date, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship
from schemas.motivo import Motivo


class Clases_no_dadas(Base):
    __tablename__ = 'CLASES_NO_DADAS'

    clase_no_dada_id = Column(Integer, primary_key=True)
    clase_id = Column(Integer, ForeignKey('CLASE.clase_id'))
    fecha_clase_no_dada = Column(Date)
    motivo = Column(Enum(Motivo, values_callable=lambda enum: [e.value for e in enum]))

    clase = relationship('Clase', backref='clases_no_dadas', lazy="joined")