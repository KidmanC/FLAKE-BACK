from config.database import Base
from sqlalchemy import Column, Date, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from schemas.grado import Grado
from schemas.tipo_identificacion import Tipo_identificacion
from schemas.genero import Genero


class Estudiante(Base):
    __tablename__ = 'ESTUDIANTE'

    estudiante_id = Column(Integer, primary_key=True)
    aula_id = Column(Integer, ForeignKey('AULA.aula_id'))
    periodo_id = Column(Integer, ForeignKey('PERIODOLECTIVO.periodo_id'))
    grado_texto = Column(Enum(Grado, values_callable=lambda enum: [e.value for e in enum]))
    grado_num = Column(Integer)
    identificacion = Column(String(20), unique=True)
    tipo_identificacion = Column(Enum(Tipo_identificacion, values_callable=lambda enum: [e.value for e in enum]))
    primer_nombre = Column(String(50))
    segundo_nombre = Column(String(50))
    primer_apellido = Column(String(50))
    segundo_apellido = Column(String(50))
    genero = Column(Enum(Genero, values_callable=lambda enum: [e.value for e in enum]))
    fecha_nacimiento = Column(Date)
    estrato = Column(Integer)

    #backref
    aula = relationship('Aula', backref='estudiantes', lazy="joined", uselist=False, join_depth=2)
    periodo = relationship('Periodo_lectivo', backref='estudiantes', lazy="joined", uselist=False, join_depth=1)

    #back_populates
    #aula = relationship('Aula', back_populates='estudiantes', lazy="joined", uselist=False, join_depth=1)
    #periodo = relationship('Periodo_lectivo', back_populates='estudiantes', lazy="joined", uselist=False, join_depth=1)
    #notas = relationship('Nota', back_populates='estudiante', lazy="joined", uselist=True, join_depth=1)
    #aula = relationship('Aula', back_populates='estudiantes', lazy="joined", uselist=False, join_depth=1)
    #asistencias = relationship('Asistencia', back_populates='estudiante', lazy="joined", uselist=True, join_depth=1)