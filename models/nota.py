from config.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship


class Nota(Base):
    __tablename__ = 'NOTA'

    nota_id = Column(Integer, primary_key=True)
    periodo_id = Column(Integer, ForeignKey('PERIODOLECTIVO.periodo_id'))
    estudiante_id = Column(Integer, ForeignKey('ESTUDIANTE.estudiante_id'))
    clase_id = Column(Integer, ForeignKey('CLASE.clase_id'))
    bloque = Column(Integer) 
    calificacion = Column(Numeric)

    #backref
    periodo = relationship('Periodo_lectivo', backref='notas', lazy="joined", uselist=False, join_depth=1)
    estudiante = relationship('Estudiante', backref='notas', lazy="selectin", uselist=False, join_depth=1)
    clase = relationship('Clase', backref='notas', lazy="selectin", uselist=False, join_depth=1)

    #back_populates
    #periodo = relationship('Periodo_lectivo', back_populates='notas', lazy="joined", uselist=False, join_depth=1)
    #estudiante = relationship('Estudiante', back_populates='notas', lazy="joined", uselist=False, join_depth=1)
    #clase = relationship('Clase', back_populates='notas', lazy="joined", uselist=False, join_depth=1)