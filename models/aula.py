from config.database import Base
from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from schemas.grado import Grado
from schemas.jornada import Jornada


class Aula(Base):
    __tablename__ = 'AULA'

    aula_id = Column(Integer, primary_key=True)
    institucion_id = Column(Integer, ForeignKey('INSTITUCION.institucion_id'))
    periodo_id = Column(Integer, ForeignKey('PERIODOLECTIVO.periodo_id'))
    grado_texto = Column(Enum(Grado, values_callable=lambda enum: [e.value for e in enum]))
    grado_num = Column(Integer)
    grupo = Column(String(10))
    jornada = Column(Enum(Jornada, values_callable=lambda enum: [e.value for e in enum]))

    institucion = relationship('Institucion', backref='aulas', lazy="joined")
    periodo = relationship('Periodo_lectivo', backref='aulas', lazy="joined")