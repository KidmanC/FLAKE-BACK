from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from schemas.tipo_identificacion import Tipo_identificacion


class Tutor(Base):
    __tablename__ = 'TUTOR'

    tutor_id = Column(Integer, primary_key=True)
    identificacion = Column(String(20))
    tipo_identificacion = Column(Enum(Tipo_identificacion, values_callable=lambda enum: [e.value for e in enum]))
    primer_nombre = Column(String(50))
    segundo_nombre = Column(String(50))
    primer_apellido = Column(String(50))
    segundo_apellido = Column(String(50))
    correo = Column(String(100))
    celular = Column(String(15))
    direccion = Column(String(150))
    periodo_id = Column(Integer, ForeignKey('PERIODOLECTIVO.periodo_id'))
    user = Column(String)
    password = Column(String)