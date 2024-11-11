from config.database import Base
from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from schemas.grado import Grado
from schemas.jornada import Jornada


class Aula(Base):
    __tablename__ = 'AULA'

    aula_id = Column(Integer, primary_key=True)
    institucion_id = Column(Integer, ForeignKey('INSTITUCION.institucion_id'))
    periodo_id = Column(Integer, ForeignKey('PERIODO.periodo_id'))
    grado_texto = Column(Enum(Grado))
    grado_num = Column(Integer)
    grupo = Column(String(10))
    Jornada = Column(Enum(Jornada))