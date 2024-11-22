from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey
from schemas.grado import Grado


class Clase(Base):
    __tablename__ = 'CLASE'

    clase_id = Column(Integer, primary_key=True)
    aula_id = Column(Integer, ForeignKey('AULA.aula_id'))
    tutor_id = Column(Integer, ForeignKey('TUTOR.tutor_id'))
    periodo_id = Column(Integer, ForeignKey('PERIODOLECTIVO.periodo_id'))
    grado = Column(Enum(Grado, values_callable=lambda enum: [e.value for e in enum]))

    #backref
    aula = relationship('Aula', backref='clases', lazy="joined", uselist=False, join_depth=1)
    tutor = relationship('Tutor', backref='clases', lazy="joined", uselist=False, join_depth=1)
    periodo = relationship('Periodo_lectivo', backref='clases', lazy="joined", uselist=False, join_depth=1)

    #back_populates
    #aula = relationship('Aula', back_populates='clases', lazy="joined", uselist=False, join_depth=1)
    #tutor = relationship('Tutor', back_populates='clases', lazy="joined", uselist=False, join_depth=1)
    #periodo = relationship('Periodo_lectivo', back_populates='clases', lazy="joined", uselist=False, join_depth=1)
    #notas = relationship('Nota', back_populates='clase', lazy="joined", uselist=True, join_depth=1)
    #horarios = relationship('Horario', back_populates='clase', lazy="joined", uselist=True, join_depth=1)
    #clases_no_dadas = relationship('Clases_no_dadas', back_populates='clase', lazy="joined", uselist=True, join_depth=1)
    #asistencias = relationship('Asistencia', back_populates='clase', lazy="joined", uselist=True, join_depth=1)
