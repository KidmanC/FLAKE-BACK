from config.database import Base
from sqlalchemy import Column, Date, Enum, Integer, String, ForeignKey
from schemas.grado import Grado
from schemas.tipo_identificacion import Tipo_identificacion
from schemas.genero import Genero


class Estudiante(Base):
    __tablename__ = 'ESTUDIANTE'

    estudiante_id = Column(Integer, primary_key=True)
    aula_id = Column(Integer, ForeignKey('AULA.aula_id'))
    periodo_id = Column(Integer, ForeignKey('PERIODO.periodo_id'))
    grado_texto = Column(Enum(Grado))
    grado_num = Column(Integer)
    identificacion = Column(String(20), unique=True)
    tipo_identificacion = Column(Enum(Tipo_identificacion))
    primer_nombre = Column(String(50))
    segundo_nombre = Column(String(50))
    primer_apellido = Column(String(50))
    segundo_apellido = Column(String(50))
    genero = Column(Enum(Genero))
    fecha_nacimiento = Column(Date)
    estrato = Column(Integer)